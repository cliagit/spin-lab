#!/usr/bin/env python3

''' Diode I-V characteristic. Keithely Source meter as current generator and Nano Voltmeter as voltage reader on channel 1'''
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
startI = 0.5E-3
# Corrente finale
endI = 200.0E-3
num = 50
# Voltaggio di protezione limite
maxVolt = 20
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
# Measurement loop
for i in I:
    # Set current of SourceMeter
    sm.write(f':SOUR:CURR:LEV {i:6.5f}')
    # Read Voltage with NanoVolt
    nanovolt.write(':READ?')
    volt = float(nanovolt.read())
    V.append(volt)
    sleep(delay)

# Turn off source meter outmput
sm.write(':OUTP OFF')

# Salvataggio
#np.save("tensione_i", V)
#np.save("corrente_i", I)

# Derivata prima
deriv1 = np.gradient(I,V)
#Derivata seconda
deriv2 = np.gradient(deriv1, V)

# Tensione di soglia max derivata seconda
#vtIndex = np.argmax(deriv2)
#print("Tensione di soglia", V[vtIndex], "V")

# Grafici
title=f'Caratteristica I-V Diodo I=[{startI:2.4f},{endI:2.4f}]' # Vt={V[vtIndex]:4.3f}'

fig, [ax, ax1, ax2] = plt.subplots(3,1)
#fig, ax = plt.subplots()
ax.plot(V, I)
#ax.plot(V[vtIndex], I[vtIndex], marker="o")
#ax.plot(V[vtIndex:],V[vtIndex:]*np.average(deriv1[vtIndex:])- np.average(deriv1[vtIndex:]))
ax1.plot(V, deriv1)
ax2.plot(V, deriv2)

ax.set(ylabel='current (A)', xlabel='voltage (V)', title=title)
ax1.set(ylabel='dA/dV', title='Derivata I')
ax2.set(xlabel='voltage (V)', ylabel='d2A/dV2',title='Derivata II')

ax.grid()
ax1.grid()
ax2.grid()

plt.show()

answer = input("Save figure? [y/N]")
if answer.upper() in ["Y", "YES"]:
	fig.savefig(title.replace(" ", "_") + ".png")

