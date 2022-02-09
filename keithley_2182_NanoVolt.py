#!/usr/bin/env python3

''' Keithely 2182 Nanovoltmeter Identify Request '''
import Gpib
# Port GPIB 0, GPIB Intrument address 7
i=Gpib.Gpib(0,7)
# Reset GPIB
i.write("*RST")
# Identify request
i.write("*IDN?")
# Read answer
print(i.read().decode("utf-8"))
