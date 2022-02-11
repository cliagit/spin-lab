#!/usr/bin/env python3

''' Lock-In Amplifier Model 5210 Identify Request '''
import Gpib
# Port GPIB 0, GPIB Intrument address 12
i=Gpib.Gpib(0,12)
# ID
i.write("ID\n")
# Read answer
print("Model:" + i.read().decode("utf-8"))
# VER
i.write("VER\n")
# Read answer
print("Version:" + i.read().decode("utf-8"))

