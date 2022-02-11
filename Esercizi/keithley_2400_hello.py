#!/usr/bin/env python3

import Gpib
inst=Gpib.Gpib(0,24)
inst.write(":DISP:WIND:TEXT:DATA 'Hellon World!'")
inst.write(":DISP:WIND2:TEXT:DATA 'Ciao a tutti :)'")
inst.write(":DISP:WIND:TEXT:STAT ON")
inst.write(":DISP:WIND2:TEXT:STAT ON")
