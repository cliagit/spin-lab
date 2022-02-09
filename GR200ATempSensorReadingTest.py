#!/usr/bin/env python3

''' 
GR-200A-250 germanium temperature sensor  
4 wires resistance measurement with Keithley 2700 or 2000
'''

import Gpib
from time import sleep
import signal
import sys
import GR200ATempSensor as sensor

def signal_handler(sig, frame):
    print('\n...graceful exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Port GPIB 0, GPIB Intrument address 16
multimeter=Gpib.Gpib(0,16)
# Reset GPIB
multimeter.write("*RST")
# Identify request
multimeter.write("*IDN?")
# Read answer
print(multimeter.read().decode("utf-8"))
# Select source function, resistance reading only.
multimeter.write(":SENS:FUNC 'FRES'")
multimeter.write(":FORM:ELEM READ")

gr200 = sensor.GR200ATempSensor()

while(True):
   # Read Resistance
   multimeter.write(':READ?')
   res = float(multimeter.read())
   temp = gr200.res_to_temp(res)
   if temp:
   	print(f"{res:.4f} Ohm temp {temp:.2f}°K {temp-273.15:.2f}°C", end='\r', flush=True)
   sleep(2)
    





