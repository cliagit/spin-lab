#!/usr/bin/env python3

''' 
Lock-In Amplifier Model 5210 Auto measure test
Select A on Sensitivity group and plug OSC OUT to A Input 
'''
import Gpib
import configparser
from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import signal
import sys

def signal_handler(sig, frame):
    print('\n...graceful exit')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


# Load configuration file
config = configparser.ConfigParser()
config.read('lock-in_5210.ini')

# Function to send Settings
def sendConfig(conf = "INIT"):
	for key in config[conf]:  
		print(key + " = " + config[conf][key])
		lockin.write(f"{key} {config[conf][key]}\n")
		sleep(0.1)


# Port GPIB 0, GPIB Intrument address 12
lockin=Gpib.Gpib(0,12)

# Ask model and version number
lockin.write("id;ver\n")
# Answer
modVer = lockin.read().decode("utf-8").split("\r\n")
print(f'Model {modVer[0]} ver {modVer[1]}')

# Send INIT Settings
sendConfig()

# Auto misura, calibrazione della sensitività e azzeramento della fase	
lockin.write("asm\n")
answer = input("Auto measure started, press a key when is completed")
sendConfig("MEASURE")
sleep(0.5)
print("Reading...")
# Nuovo ciclo di lettura su un numero di diverse misure
m = []
p = []

while(True):
	for i in range(0,10):
		lockin.write("mp\n")
		mp = lockin.read()
		mp = mp.decode("utf-8").replace("\r\n", "").split(";")
		# print("Modulo e fase:", mp)
		m.append(int(mp[0])/10000)
		p.append(int(mp[1])/1000)
		sleep(0.2)
	avgM = np.average(m)
	avgP = np.average(p)
	print(f'Modulo {avgM:.4f} V rms fase {avgP:.2f}°', end="\r")

'''
while(True):
	answer = input("Phase is < 1° [y/N] ")
	if answer.upper() in ["Y", "YES"]:
		sleep(0.5)
		print("Reading...")
		# Nuovo ciclo di lettura su un numero di diverse misure
		m = []
		p = []
		for i in range(0,20):
			lockin.write("mp\n")
			mp = lockin.read()
			mp = mp.decode("utf-8").replace("\r\n", "").split(";")
			# print("Modulo e fase:", mp)
			m.append(int(mp[0])/10000)
			p.append(int(mp[1])/1000)
			sleep(0.2)
		avgM = np.average(m)
		avgP = np.average(p)
		print(f'Modulo {avgM:.4f} V rms fase {avgP:.2f}°')
		exit(0)
	else:
		lockin.write("asm\n")
		input("Auto phase started, press a key when is completed")
		sendConfig("MEASURE")


# Ciclo di lettura modulo e fase
# Delimitatore punto e virgola
lockin.write("dd 59\n")
m = []
p = []
for i in range(0,10):
	lockin.write("mp\n")
	mp = lockin.read().decode("utf-8").replace("\r\n", "").split(";")
	m.append(int(mp[0])/10000)
	p.append(int(mp[1])/1000)
	sleep(0.2)
avgM = np.average(m)
avgP = np.average(p)
print(f'Modulo {avgM:.4f} V rms fase {avgP:.2f}°')

# Rifasatura compensazione della fase
quadrante = 0
if(avgP < 0):
	avgP = 360 + avgP
# print(avgP)
if avgP > 90 and avgP <= 180:
	quadrante = 1
	avgP = avgP - 90
if avgP > 180 and avgP <= 270:
	quadrante = 2
	avgP = avgP - 180
if avgP > 270 and avgP <= 360:
	quadrante = 3
	avgP = avgP - 270
avgP = int(avgP*1000)
# print(f'p {quadrante} {avgP}')
lockin.write(f'p {quadrante} {avgP}\n')
'''
