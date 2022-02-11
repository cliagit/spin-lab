#!/usr/bin/env python3

''' I-V characteristic. Keithely Source meter as current generator and Nano Voltmeter as voltage reader on channel 1'''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

# Nome del campione in esame
name = "CFV06G"
is4Wires = True

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
startI = 0.01E-3
# Corrente finale
endI = 1.5E-3
num = 20
# Voltaggio di protezione limite
maxVolt = 20
delay = 0.1
# Current array of num sample from start to end equally spaced
I = np.linspace(startI, endI, num)

# Togliere il commento per aggiungere la caratteristica discendente della corrente 
#I = np.concatenate((I, np.flip(I)))
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
    sleep(delay)
    # Read Voltage with NanoVolt
    nanovolt.write(':READ?')
    volt = float(nanovolt.read())
    V.append(volt)
    

# Turn off source meter output
sm.write(':OUTP OFF')

# Derivata prima
grad1 = np.gradient(V, I)
#Derivata seconda
#deriv2 = np.gradient(deriv1, V)

maxV = np.max(V)
maxVIndex = np.argmax(V)

# Grafici
if maxVIndex > num - 2:
	title=f'{name} I=[{startI:.2e},{endI:.2e}] \n delay {delay} samples {num}'
else:
	title=f'{name} I=[{startI:.2e},{endI:.2e}] Vmax={maxV:.2e} at I={I[maxVIndex]:.2e}\n delay {delay} samples {num}'
if is4Wires:
	title += " Wires 4"

fig, [ax, ax1, ax2] = plt.subplots(3,1)
#fig, [ax, ax1] = plt.subplots(2,1)
ax.plot(V, I)

ax1.plot(I,V)

if maxVIndex < num - 2:
	ax1.plot(I[maxVIndex], V[maxVIndex], marker="o")

ax2.plot(I,V/I)

# ax3.plot(I, grad1)
# print(np.average(grad1))
''' #Scala Logaritmica
ax.set(ylabel='current (A)', xlabel='voltage (V)', title=title, yscale='log', xscale='log')
ax1.set(xlabel='current (A)', ylabel='voltage (V)', yscale='log', xscale='log')
ax2.set(xlabel='current (A)', ylabel='R (Ohm)', xscale='log')
'''
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

