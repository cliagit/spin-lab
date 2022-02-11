#!/usr/bin/env python3

''' Keithely source variable voltage test '''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

start = -5.0
end = 5.0
num = 100
limiti = 10E-3
delay = 0.01

# Port GPIB 0, GPIB Intrument address 24
ins=Gpib.Gpib(0,24)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
# Read answer from device
print(ins.read().decode('utf-8'))

# Voltage array of num sample from start to end equally spaced 
V = np.linspace(start, end, num)

''' Select source function, mode '''
#Select voltage source.
ins.write(":SOUR:FUNC VOLT")
''' Set source range, level, compliance ''' 
# Select 20V source range.
ins.write(':SOUR:VOLT:RANG 20')
# 10mA compliance.
ins.write(f':SENS:CURR:PROT {limiti}')
# Current measure function.
ins.write(":SENS:FUNC 'CURR'")
''' Set measure function, range '''
# 10mA measure range.
ins.write(f':SENS:CURR:RANG {limiti}')
# Current reading only.
ins.write(":FORM:ELEM CURR")
# Turn on output
ins.write(":OUTP ON")

''' Loop over array V, send V samples and reading I measures '''
# Array of current measures
I = []
for i in V:
    ins.write(f':SOUR:VOLT:LEV {i}')
    sleep(delay)
    ins.write(':READ?')
    cur = float(ins.read())
    I.append(cur)

ins.write(':OUTP OFF')

# Stima della resistenza
print("Resistenza:", np.average(V/I), 'ohm')
print("Resistenza:", np.average(np.gradient(V,I)), 'ohm')


fig, ax = plt.subplots()

ax.plot(V, I)
title=f'Caratteristica I-V Resistore V=[{start},{end}] res={int(np.average(np.gradient(V,I)))}ohm'
ax.set(xlabel='Voltage (V)', ylabel='Current (A)',
       title=title)
ax.grid()

plt.show()

answer = input("Save figure? [y/N] ")
if answer.upper() in ["Y", "YES"]:
	fig.savefig(title.replace(" ", "_")+".png")

