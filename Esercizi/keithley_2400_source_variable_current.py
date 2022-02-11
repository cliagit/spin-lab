#!/usr/bin/env python3

''' Keithely caratteristica con corrente variabile '''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

# Corrente iniziale
start = -15.0E-3
# Corrente finale
end = 15.0E-3
num = 100
# Voltaggio limite
limiti = 0.05
delay = 0.01

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
ins.write(':SOUR:CURR:RANG {}'.format(end - start))
# Voltage compliance.
ins.write(':SENS:VOLT:PROT {}'.format(limiti))
# Voltage measure function.
ins.write(":SENS:FUNC 'VOLT'")
''' Set measure function, range '''
# Voltage measure range.
ins.write(':SENS:VOLT:RANG {}'.format(limiti))
# Current reading only.
ins.write(":FORM:ELEM VOLT")
# Turn on output
ins.write(":OUTP ON")

# Array of voltage measures
V = []
for i in I:
    ins.write(f':SOUR:CURR:LEV {i:6.5f}')
    ins.write(':READ?')
    volt = float(ins.read())
    V.append(volt)
    sleep(delay)

ins.write(':OUTP OFF')

# Stima della resistenza
print("Resistenza:", np.average(V/I), 'ohm')
print("Resistenza:", np.average(np.gradient(V,I)), 'ohm')


fig, ax = plt.subplots()
ax.grid()
ax.plot(V, I)
title=f'Caratteristica I-V Resistore I=[{start},{end}] res={np.average(np.gradient(V,I)):4.3f} ohm'
ax.set(xlabel='Voltage (V)', ylabel='Current (A)',
       title=title)

plt.show()

answer = input("Save figure? [y/N] ")
if answer.upper() in ["Y", "YES"]:
	fig.savefig(title.replace(" ", "_") + ".png")
