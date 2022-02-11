#!/usr/bin/env python3
''' Keithely 2700 Multimeter Reading test '''
import Gpib
from time import sleep
import signal
import sys

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

while(True):
    # Read Voltage
    multimeter.write(':READ?')
    volt = float(multimeter.read())
    print(f"Voltage: {volt:.4f}V", end='\r', flush=True)
    sleep(2)
    






