#!/usr/bin/env python3

''' 
Silicon diode temperature sensor Lake Shore DT-470 model 
2 wires voltage measurement with Keithley 2700 or 2000
'''

import Gpib
from time import sleep
import signal
import sys
from lib import DT400TempSensor as sensor

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
# Select source function, mode Voltage reading only.
multimeter.write(":SENS:FUNC 'VOLT'")
# CHANNEL 1
# multimeter.write(":SENS:CHAN 1")
multimeter.write(":FORM:ELEM READ")

dt400 = sensor.DT400TempSensor()

while(True):
    # Read Voltage
    multimeter.write(':READ?')
    volt = float(multimeter.read())
    temp = dt400.voltage_to_temp(volt)
    print(f"{volt:.5f}V temp {temp:.2f}°K {temp-273.16:.2f}°C", end='\r', flush=True)
    sleep(2)
    





