#!/usr/bin/env python3

''' Keithely source fixed current setting '''
import Gpib
from time import sleep
# Port GPIB 0, GPIB Intrument address 24
ins=Gpib.Gpib(0,24)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
# Read answer
print(ins.read().decode('utf-8'))
''' Select source function, mode '''
#Select current source.
ins.write(":SOUR:FUNC CURR")
''' Set source range, level, compliance ''' 
# Select source range.
ins.write(":SOUR:CURR:RANG 10E-3")
# Source output.
ins.write(":SOUR:CURR:LEV 5E-3")
# 30V compliance.
ins.write(":SENS:VOLT:PROT 30")
# Voltage measure function.
ins.write(":SENS:FUNC 'VOLT'")
''' Set measure function, range ''' 
# 30V measure range.
ins.write(":SENS:VOLT:RANG 30")
# Voltage reading only.
ins.write(":FORM:ELEM VOLT")
# Turn on output
ins.write(":OUTP ON")
# Read data, Trigger, acquire reading.
ins.write(":READ?")
#print(ins.read())
# Read answer
V=float(ins.read())
print("Measured voltage: {0}V Resistance {1} ohm".format(V, V/0.005))
# wait in seconds
sleep(10)
# Turn off output
ins.write(":OUTP OFF")
