
#!/usr/bin/env python3
''' 
PT100 diode temperature sensor  
4 wires resistance measurement with Keithley 2700 or 2000
'''

import Gpib
from time import sleep
import signal
import sys
import PT100TempSensor as sensor

def signal_handler(sig, frame):
    print('...graceful exit')
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

pt100 = sensor.PT100TempSensor()

while(True):
   # Read Resistance
   multimeter.write(':READ?')
   res = float(multimeter.read())
   temp = pt100.res_to_temp(res)
   if temp:
   	temp1 = pt100.res_to_temp_formula(res)
   	print(f"{res:.4f} Ohm temp {temp:.2f}°K {temp-273.15:.2f}°C formula:{temp1:.2f}°K", end='\r', flush=True)
   sleep(2)
    





