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
import signal
import sys
import os
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import Gpib
from lib import DT400TempSensor as sensor

plt.style.use('dark_background')

# Load configuration file
config = configparser.ConfigParser()
config.read('exp_i_v_fixed_current_variable_temperature.ini')
conf = config['DEFAULT']

# Nome del campione in esame
SAMPLE_NAME = conf['SAMPLE_NAME']

# Current fixed source
SOURCE_I = float(conf['SOURCE_I'])

# Collegamenti del campione a 4 fili
IS_4_WIRES = conf['IS_4_WIRES']

# Intervallo di acquisizione
DELAY = float(conf['DELAY'])

title = f"{SAMPLE_NAME} fixed current {conf['SOURCE_I']}A" 

# Inizializzazione del sensore di temperatura al silicio
dt400 = sensor.DT400TempSensor()

### Configurazione del multimetro Keithley 2700
# Port GPIB 0, GPIB Intrument address 16
multimeter=Gpib.Gpib(0,16, 20)
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

### Configurazione del nano voltmeter Keithley 2182A
# Port GPIB 0, GPIB Intrument address 7
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

### Configurazione del SourceMeter Keithley 2400
# Port GPIB 0, GPIB Intrument address 24
sm=Gpib.Gpib(0,24)
# Reset GPIB defaults
sm.write("*RST")
# Identify request
sm.write("*IDN?")
# Read answer from device
print(sm.read().decode('utf-8'))

### Select source function, mode '''
#Select current source.
sm.write(":SOUR:FUNC CURR")
# Select source range.
#sm.write(":SOUR:CURR:RANG 10E-3")
# Source output.
sm.write(f":SOUR:CURR:LEV {SOURCE_I:6.5f}")
# Voltage compliance.
sm.write(f':SENS:VOLT:PROT {conf["MAX_VOLT"]}')
# Voltage measure function.
sm.write(":SENS:FUNC 'VOLT'")

# Turn on source meter output
sm.write(":OUTP ON")

### Measurement thread loop ###
exit_event = threading.Event()

def measure_thread_function():
    n = 10
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
        voltSum = 0.0
        tempSum = 0.0
        # Media su n misure
        for i in range(n):
            # print(i)
            # Read Voltage with NanoVolt
            nanovolt.write(':READ?')
            voltSum += float(nanovolt.read())
            sleep(DELAY)
            # Read temperature
            multimeter.write(':READ?')
            tempSum += dt400.voltage_to_temp(float(multimeter.read()))
            sleep(DELAY)
        temp = tempSum/n
        volt = voltSum/n
        res = volt/SOURCE_I
        print(f'T:{temp:.2f}K V:{volt:.3f}V R:{res:.3f} Ohm', end="\r")
        # Update voltage array
        V.append(volt)
        # Update resistance array
        R.append(res)
        # Update temperature array
        T.append(temp)
        # Update datetime array
        DT.append(datetime.now())
        if exit_event.is_set():
            print("\nStop Measuring\n")
            break
 
#         
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

# animation function.  This is called sequentially
def animate(i):
    # print(i, T, R) # , T[i], R[i])
    ax.plot(T[:i], R[:i], 'o-', color='orange')
    ax1.plot(DT[:i], V[:i], 'o-', color='orange')
    ax2.plot(DT[:i], T[:i], 'o-', color='orange')
    
def on_close(event):
    # Turn off source meter output
    sm.write(':OUTP OFF')
    # print('\n...graceful exit')
    exit_event.set()
    thr.join()
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    answer = input("Save data? [y/N]")
    if answer.upper() in ["Y", "YES"]:
        path = title.replace(" ", "_")
        try: 
            os.mkdir(path) 
        except OSError as error: 
            print(error)  
        # Salvataggio dati
        np.savez_compressed(path + "/" + path + "-" + date_time, datetime=DT, temperature=T, voltage=V, resistance=R, current_source=SOURCE_I)
        # Salvataggio grafico
        fig.savefig(path + "/" + path + "-" + date_time + ".png")
    sys.exit(0)

anim = animation.FuncAnimation(plt.gcf(), animate, interval=500, blit=False)

# Gestione dell'evento della chiusura della finestra
fig.canvas.mpl_connect('close_event', on_close)

plt.show()

"""
np.stack((VIData['resistance'], VIData['temperature']), axis=-1)
date_time = datetime.now().strftime("%Y%m%d%H%M%S")

answer = input("Save figure? [y/N]")
if answer.upper() in ["Y", "YES"]:
    # Salvataggio dati
    np.savez_compressed(title.replace(" ", "_") + "-" + date_time, V=V, I=I)
    # Salvataggio grafico
    fig.savefig(title.replace(" ", "_") + "-" + date_time + ".png")
"""
