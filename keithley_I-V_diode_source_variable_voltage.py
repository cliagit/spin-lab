#!/usr/bin/env python3

''' Keithely Caratteristica I-V diodo con voltaggio variabile'''
import Gpib
from time import sleep
import numpy as np
from matplotlib import pyplot as plt

start = -1.0
end = 1.0
num = 100
curr_limit = 500E-3
delay = 0.01

# Port GPIB 0, GPIB Intrument address 24
ins=Gpib.Gpib(0,24)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
# Read answer
print(ins.read().decode('utf-8'))

# Voltage array of num sample from start to end equally spaced 
V = np.linspace(start, end, num)

''' Select source function, mode '''
#Select voltage source.
ins.write(":SOUR:FUNC VOLT")
''' Set source range, level, compliance ''' 
# Select source range.
ins.write(':SOUR:VOLT:RANG {}'.format(end -start))
# 200mA compliance.
ins.write(':SENS:CURR:PROT {}'.format(curr_limit))
# Current measure function.
ins.write(":SENS:FUNC 'CURR'")
''' Set measure function, range '''
# 20mA measure range.
ins.write(':SENS:CURR:RANG {}'.format(curr_limit))
# Current reading only.
ins.write(":FORM:ELEM CURR")
# Turn on output
ins.write(":OUTP ON")

''' Loop over array V, send V samples and reading I measures '''
# Array of current measures
I = []
for i in V:
    ins.write(':SOUR:VOLT:LEV {}'.format(i))
    sleep(delay)
    ins.write(':READ?')
    cur = float(ins.read())
    I.append(cur)

ins.write(':OUTP OFF')

# Salvataggio
#np.save("tensione_v", V)
#np.save("corrente_v", I)

# Derivata prima
deriv1 = np.gradient(I,V)
#Derivata seconda
deriv2 = np.gradient(deriv1, V)

# Tensione di soglia max derivata seconda
vtIndex = np.argmax(deriv2)
print(V[vtIndex], "V")

# Grafici
fig, [ax, ax1, ax2] = plt.subplots(3,1)
ax.plot(V, I)
ax.plot(V[vtIndex],I[vtIndex], marker="o")
#ax.plot(V[vtIndex:],V[vtIndex:]*np.average(deriv1[vtIndex:])- np.average(deriv1[vtIndex:]))
ax1.plot(V, deriv1)
ax2.plot(V, deriv2)


ax.set(ylabel='current (A)',
        title=f'Caratteristica I-V Diodo V=[{start},{end}] Vt={V[vtIndex]:4.3f}')
ax1.set(ylabel='dA/dV',
       title='Derivata I')
ax2.set(xlabel='voltage (V)', ylabel='d2A/dV2',
       title='Derivata II')

ax.grid()
ax1.grid()
ax2.grid()
plt.show()

answer = input("Save figure? [y/N]")
if answer.upper() in ["Y", "YES"]:
	fig.savefig(title.replace(" ", "_") + ".png")

