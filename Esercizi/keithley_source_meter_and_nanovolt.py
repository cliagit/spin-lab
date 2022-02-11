#!/usr/bin/env python3

''' Resistor characteristic. Keithely Source meter as current generator and Nano Voltmeter as voltage reader on channel 1'''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
''' Configurazione del nano voltmeter Keithley 2182A '''
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

''' Configurazione del SourceMeter Keithley 2400 '''
# Port GPIB 0, GPIB Intrument address 24
sm=Gpib.Gpib(0,24)
# Reset GPIB defaults
sm.write("*RST")
# Identify request
sm.write("*IDN?")
# Read answer from device
print(sm.read().decode('utf-8'))
# Corrente iniziale
startI = -20.0E-3
# Corrente finale
endI = 20.0E-3
num = 50
# Voltaggio di protezione limite
maxVolt = 0.05
delay = 0.1
# Current array of num sample from start to end equally spaced
I = np.linspace(startI, endI, num)
# print(I)

''' Select source function, mode '''
#Select current source.
sm.write(":SOUR:FUNC CURR")
''' Set source range, level, compliance ''' 
# Select source range.
sm.write(':SOUR:CURR:RANG {}'.format(endI - startI))
# Voltage compliance.
sm.write(':SENS:VOLT:PROT {}'.format(maxVolt))
# Voltage measure function.
sm.write(":SENS:FUNC 'VOLT'")

# Turn on source meter output
sm.write(":OUTP ON")

# Array of voltage measures
V = []
R = []
# Measurement loop
for i in I:
    # Set current of SourceMeter
    sm.write(f':SOUR:CURR:LEV {i:6.5f}')
    # Read Voltage with NanoVolt
    nanovolt.write(':READ?')
    volt = float(nanovolt.read())
    V.append(volt)
    R.append(volt/i)
    sleep(delay)

# Turn off source meter outmput
sm.write(':OUTP OFF')

# Stima della resistenza
print("Resistenza:", np.average(R), 'ohm')
print("Resistenza:", np.average(np.gradient(V,I)), 'ohm')


fig, ax = plt.subplots()
ax.grid()
ax.plot(V, I)
title=f'Caratteristica I-V Resistore I=[{startI},{endI}] res={np.average(np.gradient(V,I)):4.3f} ohm'
ax.set(xlabel='Voltage (V)', ylabel='Current (A)',
       title=title)

plt.show()

answer = input("Save figure? [y/N] ")
if answer.upper() in ["Y", "YES"]:
	fig.savefig(title.replace(" ", "_") + ".png")

