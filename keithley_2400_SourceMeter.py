#!/usr/bin/env python3

''' Keithely 2400 Source Meter Identify Request '''
import Gpib
# Port GPIB 0, GPIB Intrument address 24
i=Gpib.Gpib(0,24)
# Reset GPIB
i.write("*RST")
# Identify request
i.write("*IDN?")
# Read answer
print(i.read().decode("utf-8"))
