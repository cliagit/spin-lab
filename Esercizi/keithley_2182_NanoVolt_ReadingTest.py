#!/usr/bin/env python3

''' Keithely Nano Voltmeter reading both channels '''
import Gpib
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    print('\n...graceful exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Port GPIB 0, GPIB Intrument address 7
ins=Gpib.Gpib(0,7)
# Reset GPIB defaults
ins.write("*RST")
# Identify request
ins.write("*IDN?")
# Read answer
print(ins.read().decode('utf-8'))
''' Select source function, mode '''
# Voltage reading only.
ins.write(":SENS:FUNC 'VOLT'")


while(True):
    # CHANNEL 1
#ins.write(":SENS:FUNC 'VOLT:DC'")
    ins.write(":SENS:CHAN 1")
    ins.write(":READ?")
    # Read answer
    V1=float(ins.read())
    # CHANNEL 2
    # sleep(.200)
    #ins.write(":SENS:FUNC 'VOLT:DC'")
    ins.write(":SENS:CHAN 2")
    ins.write(":READ?")
    # Read answer
    V2=float(ins.read())
    print(f"Measured voltage CH1 {V1}V CH2 {V2}V", end="\r")
    # wait in seconds
    sleep(2)
