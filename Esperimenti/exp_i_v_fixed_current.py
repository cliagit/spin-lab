#!/usr/bin/env python3

'''
 I-V characteristic. Keithely Source meter as fixed current generator and
 Nano Voltmeter as voltage reader on channel 1
 Keithely multimeter 2000 or 2700 to measure temperature with silicon diode
'''
from datetime import datetime
from time import sleep
import threading
import configparser
import sys
import os
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
import numpy as np
import gpib
import Gpib
from lib import DT400TempSensor as sensor

plt.style.use('dark_background')

# Load configuration file
config = configparser.ConfigParser()
config.read('exp_i_v_fixed_current.ini')
conf = config['DEFAULT']

# Nome del campione in esame
SAMPLE_NAME = conf['SAMPLE_NAME']

# Current fixed source
SOURCE_I = float(conf['SOURCE_I'])

# Intervallo di acquisizione
DELAY = float(conf['DELAY'])

title = f"{SAMPLE_NAME} fixed current {conf['SOURCE_I']}A"

# Inizializzazione del sensore di temperatura al silicio
dt400 = sensor.DT400TempSensor()

### Configurazione del multimetro Keithley 2700
# Port GPIB 0, GPIB Intrument address 16
try:
    multimeter=Gpib.Gpib(0,16)
    # Reset GPIB
    multimeter.write("*RST")
    # Identify request
    multimeter.write("*IDN?")
    # Read answer
    print(multimeter.read().decode("utf-8"))
    # Select source function, mode Voltage reading only.
    multimeter.write(":SENS:FUNC 'VOLT'")
    # CHANNEL 1
    multimeter.write(":FORM:ELEM READ")
except gpib.GpibError as e:
    print("Oops!", e, "occurred.")
    print("Multimeter doesn't respond, check it out!")
    sys.exit(-1)


### Configurazione del nano voltmeter Keithley 2182A
# Port GPIB 0, GPIB Intrument address 7
try:
    nanovolt=Gpib.Gpib(0,7)
    # Reset GPIB defaults
    nanovolt.write("*RST")
    # Identify request
    nanovolt.write("*IDN?")
    # Read answer
    print(nanovolt.read().decode('utf-8'))
    # Select source function, mode Voltage reading only.
    nanovolt.write(":SENS:FUNC 'VOLT'")
    # CHANNEL 1
    nanovolt.write(":SENS:CHAN 1")
except gpib.GpibError as e:
    print("Oops!", e, "occurred.")
    print("Nanovolt meter doesn't respond, check it out!")
    sys.exit(-1)

### Configurazione del SourceMeter Keithley 2400
# Port GPIB 0, GPIB Intrument address 24
#try:
#    sm=Gpib.Gpib(0,24)
#    # Reset GPIB defaults
#    sm.write("*RST")
#    # Identify request
#    sm.write("*IDN?")
#    # Read answer from device
#    print(sm.read().decode('utf-8'))
#### Select source function, mode '''
#    #Select current source.
#    sm.write(":SOUR:FUNC CURR")
#    # Select source range.
#    #sm.write(":SOUR:CURR:RANG 10E-3")
#    # Source output.
#    sm.write(f":SOUR:CURR:LEV {SOURCE_I:6.5f}")
#    # Voltage compliance.
#    sm.write(f':SENS:VOLT:PROT {conf["LIM_VOLT"]}')
#    # Voltage measure function.
#    sm.write(":SENS:FUNC 'VOLT'")
#    # Voltage reading only.
#    sm.write(":FORM:ELEM VOLT")
#    # Turn on source meter output
#    sm.write(":OUTP ON")
#    pass
#except gpib.GpibError as e:
#    print("Oops!", e, "occurred.")
#    print("Source meter doesn't respond, check it out!")
#    sys.exit(-1)

### Configurazione del SourceMeter Keithley 6220
# Port GPIB 0, GPIB Intrument address 12
try:
    sm=Gpib.Gpib(0,12)
    # Reset GPIB defaults
    sm.write("*RST")
    # Identify request
    sm.write("*IDN?")
    # Read answer
    print(sm.read().decode('utf-8'))
    sm.write(":CLE")
    # Select source range.
    sm.write(":SOUR:CURR:RANG:AUTO ON")
    # Source output.
    sm.write(f":SOUR:CURR {conf['SOURCE_I']}")
    # Compliance.voltage limit
    sm.write(f':SOUR:CURR:COMP {conf["LIM_VOLT"]}')
    # Turn on output
    sm.write(":OUTP ON")
except gpib.GpibError as e:
    print("Oops!", e)
    print("Source meter 6220 doesn't respond, check it out!")
    sys.exit(-1)

# Instantiate threading event handler
exit_event = threading.Event()

def measure_thread_function():
    """ Measurement thread """
    n = 20
    # Array of resistence values
    global R
    R = []
    # Array of temperature measures
    global T
    T = []
    # Array of datetime
    global DT
    DT = []
    # Array of voltage measures
    global V
    V= []
    print("\nStart measurement loop\n")
    # Measurement loop
    while True:
        error = False
        volt_sum = 0.0
        temp_sum = 0.0
        # Media su n misure
        for i in range(n):
            try:
                # print(i)
                # Read Voltage with NanoVolt
                nanovolt.write(':READ?')
                volt_sum += float(nanovolt.read())
                # sleep(DELAY)
                # Read temperature
                multimeter.write(':READ?')
                temp_sum += dt400.voltage_to_temp(float(multimeter.read()))
                sleep(DELAY)
                error = False
            except ValueError:
                error = True
                print("Temperature out of range!")
                break
            except gpib.GpibError as e:
                print("Oops!", e)
                error = True
                print("Error data reading, check the instruments")
                break
        if not error:
            temp = temp_sum/n
            volt = volt_sum/n
            res = volt/SOURCE_I
#            try:
#                # Lettura del voltaggio misurato al Source Meter 2400
#                sm.write(':READ?')
#                voltSm = float(sm.read())
#                lim = float(conf["LIM_VOLT"])
#                print(f'T:{temp:.2f}K V:{volt:.3f}V R:{res:.3f} Ohm Voltage limit: {(voltSm*100)/lim:.2f}%', end="\r")
#            except:
#                print(f'T:{temp:.2f}K V:{volt:.3f}V R:{res:.3f} Ohm                                      ', end="\r")
#                print("\nSource meter reading error!\n")

            print(f'T:{temp:.2f}K V:{volt:.3f}V R:{res:.3f} Ohm                         ', end="\r")
            # Update voltage array
            V.append(volt)
            # Update resistance array
            R.append(res)
            # Update temperature array
            T.append(temp)
            # Update datetime array
            DT.append(datetime.now())
        # Thread exits
        if exit_event.is_set():
            print("\nEnd of measurement loop\n")
            break

# Start Measurement thread loop
thr = threading.Thread(target=measure_thread_function)
thr.start()

### Plotting ###
fig, [ax, ax1, ax2] = plt.subplots(3,1)
ax.set(ylabel='Resistance [Ohm]', xlabel='Temperature [K]', title=title) # , yscale='log', xscale='log')
ax1.set(ylabel='Voltage [V]', xlabel='Time') # , yscale='log', xscale='log')
ax2.set(ylabel='Temperature [K]', xlabel='Time') # , yscale='log', xscale='log')

ax.grid()
ax1.grid()
ax2.grid()

# Lista delle annotazioni
ann_list = []

def animate(i):
    """ animation function.  This is called sequentially """
   # print(i, T[i], R[i])
    ax.plot(T[:i], R[:i], 'o-', color='orange')
    ax1.plot(DT[:i], V[:i], 'o-', color='red')
    ax2.plot(DT[:i], T[:i], 'o-', color='yellow')
    if len(T) > 0:
        # Rimozione delle annotazioni precedenti
        for i, a in enumerate(ann_list):
            a.remove()
        ann_list[:] = []
        # Annotazione ultimo valore misurato
        an = ax.annotate(f'{R[-1]:.2e}', xy=(1.05, 0.9),  xycoords='axes fraction', color="orange")
        an1 = ax1.annotate(f'{V[-1]:.2e}', xy=(1.05, 0.9),  xycoords='axes fraction', color="r")
        an2 = ax2.annotate(f'{T[-1]:.2e}', xy=(1.05, 0.9),  xycoords='axes fraction', color="y")
        ann_list.append(an)
        ann_list.append(an1)
        ann_list.append(an2)
        


def on_close(event):
    """ On close plotting window event handler """
    # Trigger thread exit event
    exit_event.set()
    thr.join()
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    answer = input("Save data? [y/N]")
    if answer.upper() in ["Y", "YES"]:
        path = title.replace(" ", "_")
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                # Create and save README file descriptor
                with open(path + "/README", "a", "UTF-8") as file:
                    file.write(conf['DESCRIPTION'])
                    file.write(f"\nNome del campione: {conf['SAMPLE_NAME']}")
                    file.write(f"\nValore della corrente sorgente: {conf['SOURCE_I']}")
        except OSError as error:
            print(error)
        # Salvataggio dati formato numpy
        np.savez_compressed(path + "/" + path + "-" + date_time, datetime=DT, temperature=T,
                            voltage=V, resistance=R, current_source=SOURCE_I)

        # Salvataggio dati formato csv
        data = pd.DataFrame(np.stack((T,R,V), axis=-1), 
               columns=['Temperature', 'Resistance', 'Voltage'])
        data.to_csv(path + "/" + path + "-" + date_time + ".csv", index=False)

        # Salvataggio grafico
        fig.savefig(path + "/" + path + "-" + date_time + ".png")
    try:
        # Turn off source meter output
        sm.write(':OUTP OFF')
    except gpib.GpibError:
        print("Source meter doesn't respond, check it out!")
        sys.exit(-1)
    sys.exit(0)

anim = animation.FuncAnimation(plt.gcf(), animate, interval=500, blit=False)

# Impostazione dell'evento della chiusura della finestra
fig.canvas.mpl_connect('close_event', on_close)

plt.show()