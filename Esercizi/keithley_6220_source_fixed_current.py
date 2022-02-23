#!/usr/bin/env python3

''' Keithely 6220 source fixed current setting '''
import Gpib
from time import sleep
# Port GPIB 0, GPIB Intrument address 12
ins=Gpib.Gpib(0,12)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
## Read answer
print(ins.read().decode('utf-8'))
#''' Set source range, level, compliance ''' 
ins.write(":CLE")
## Select source range.
ins.write(":SOUR:CURR:RANG:AUTO ON")
## Source output.
ins.write(":SOUR:CURR 5E-3")
## 10V compliance.
ins.write(":SOUR:CURR:COMP 10")
## Turn on output
ins.write(":OUTP ON")
sleep(10)
## Turn off output
ins.write(":OUTP OFF")
