#!/usr/bin/env python3

'''
 I-V characteristic. Keithely Source meter as fixed current generator and
 Nano Voltmeter as voltage reader on channel 1
 Keithely multimeter 2000 or 2700 to measure temperature with silicon diode
'''
from datetime import datetime
from time import sleep
import configparser
import signal
import sys
from matplotlib import pyplot as plt
import numpy as np
import Gpib
from lib import DT400TempSensor as sensor


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

# Inizializzazione del sensore di temperatura al silicio
dt400 = sensor.DT400TempSensor()


### Configurazione del multimetro Keithley 2700
# Port GPIB 0, GPIB Intrument address 16
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

# Array of resistence measures
R = []
# Array of temperature measures
T = []

fig, [ax, ax1] = plt.subplots(2,1)
line, = ax.plot([], [], lw=2)
line.set_data(T, R)


# Measurement loop
while True:
    volt = 0.0
    temp = 0.0
    # Media su 20 misure
    for i in range(1,20):
        # Read Voltage with NanoVolt
        nanovolt.write(':READ?')
        volt += float(nanovolt.read())
        # Read temperature
        multimeter.write(':READ?')
        temp += dt400.voltage_to_temp(float(multimeter.read()))
        sleep(DELAY)

    # Compute resistance
    R.append(volt/(20*SOURCE_I))
    # Read temperature
    T.append(temp/20)

# Turn off source meter output
sm.write(':OUTP OFF')

def signal_handler(sig, frame):
    """ Gestione uscita dal programma con Ctrl+C """
    print('\n...graceful exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Grafici
#if maxVIndex > NUM - 2:
#    title=f'{SAMPLE_NAME} I=[{START_I:.2e},{END_I:.2e}] \n DELAY {DELAY} samples {NUM}'
#else:
#    title=f'{SAMPLE_NAME} I=[{START_I:.2e},{END_I:.2e}] Vmax={maxV:.2e} at I={I[maxVIndex]:.2e}\n'
# + 'DELAY {DELAY} samples {NUM}'
#if IS_4_WIRES:
#    title += " Wires 4"
"""
fig, [ax, ax1] = plt.subplots(2,1)
ax.plot(V, I)

ax1.plot(I,V)

ax2.plot(I,V/I)

# ax3.plot(I, grad1)
# print(np.average(grad1))

##Scala Logaritmica
#ax.set(ylabel='current (A)', xlabel='voltage (V)', title=title, yscale='log', xscale='log')
#ax1.set(xlabel='current (A)', ylabel='voltage (V)', yscale='log', xscale='log')
#ax2.set(xlabel='current (A)', ylabel='R (Ohm)', xscale='log')

# Scala Lineare
ax.set(ylabel='current (A)', xlabel='voltage (V)', title=title)
ax1.set(xlabel='current (A)', ylabel='voltage (V)')
ax2.set(xlabel='current (A)', ylabel='R (Ohm)')

ax.grid()
ax1.grid()
ax2.grid()
# ax3.grid()

plt.show()

date_time = datetime.now().strftime("%Y%m%d%H%M%S")

answer = input("Save figure? [y/N]")
if answer.upper() in ["Y", "YES"]:
    # Salvataggio dati
    np.savez_compressed(title.replace(" ", "_") + "-" + date_time, V=V, I=I)
    # Salvataggio grafico
    fig.savefig(title.replace(" ", "_") + "-" + date_time + ".png")
"""
