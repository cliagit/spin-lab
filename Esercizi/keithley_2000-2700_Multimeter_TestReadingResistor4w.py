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
# Select source function, resistance reading only.
multimeter.write(":SENS:FUNC 'FRES'")
# CHANNEL 1
# multimeter.write(":SENS:CHAN 1")
multimeter.write(":FORM:ELEM READ")

while(True):
    # Read Resistance
    multimeter.write(':READ?')
    res = float(multimeter.read())
    print(f"Resistance:{res:.4f} Ohm", end="\r")
    sleep(2)
    






