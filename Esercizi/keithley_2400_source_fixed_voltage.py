#!/usr/bin/env python3

''' Keithely source fixed voltage setting '''
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
#Select voltage source.
ins.write(":SOUR:FUNC VOLT")
# Fixed voltage source mode.
ins.write(":SOUR:VOLT:MODE FIXED")
''' Set source range, level, compliance ''' 
# Select 20V source range.
ins.write(":SOUR:VOLT:RANG 20")
# Source output = 10V.
ins.write(":SOUR:VOLT:LEV 10.0000")
# 10mA compliance.
ins.write(":SENS:CURR:PROT 10E-3")
# Current measure function.
ins.write(":SENS:FUNC 'CURR'")
''' Set measure function, range '''
# 10mA measure range.
ins.write(":SENS:CURR:RANG 10E-3")
# Current reading only.
ins.write(":FORM:ELEM CURR")
# Turn on output
ins.write(":OUTP ON")
# Read data, Trigger, acquire reading.
ins.write(":READ?")
# Read answer
I=float(ins.read())
print("Current measured: {0}A Resistance {1}".format(I, 10/I))
# wait in seconds
sleep(10)
# Turn off output
ins.write(":OUTP OFF")
