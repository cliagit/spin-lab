#! /usr/bin/python3
""" Keithely 2700 Multimeter Identify Request """
import Gpib
# Port GPIB 0, GPIB Instrument address 16
i=Gpib.Gpib(0,16)
# Reset GPIB
try:
  i.write("*RST")
except Exception as err:
  print("Errore di time out")

# Identify request
i.write("*IDN?")
# Read answer
print(i.read().decode("utf-8"))
