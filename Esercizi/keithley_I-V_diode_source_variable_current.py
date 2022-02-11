#!/usr/bin/env python3

''' Keithely 2400 source variable current test '''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

# Corrente iniziale
start = 0.5E-3
# Corrente finale
end = 400.0E-3
num = 100
# Voltaggio limite
limiti = 20
delay = 0.1

# Port GPIB 0, GPIB Intrument address 24
ins=Gpib.Gpib(0,24)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
# Read answer from device
print(ins.read().decode('utf-8'))

# Current array of num sample from start to end equally spaced
I = np.linspace(start, end, num)

''' Select source function, mode '''
#Select current source.
ins.write(":SOUR:FUNC CURR")
''' Set source range, level, compliance ''' 
# Select source range.
ins.write(f':SOUR:CURR:RANG {end - start}')
# Voltage compliance.
ins.write(f':SENS:VOLT:PROT {limiti}')
# Voltage measure function.
ins.write(":SENS:FUNC 'VOLT'")
''' Set measure function, range '''
# Voltage measure range.
ins.write(f':SENS:VOLT:RANG {limiti}')
# Current reading only.
ins.write(":FORM:ELEM VOLT")
# Turn on output
ins.write(":OUTP ON")

# Array of voltage measures
V = []
for i in I:
    ins.write(f':SOUR:CURR:LEV {i:6.5f}')
    sleep(delay)
    ins.write(':READ?')
    volt = float(ins.read())
    V.append(volt)

ins.write(':OUTP OFF')


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
title=f'Caratteristica I-V Diodo I=[{start:2.4f},{end:4.3f}]' # Vt={V[vtIndex]:4.3f}'

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

