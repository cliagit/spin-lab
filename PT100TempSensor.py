"""
Implementation of calibration curve DIN IEC 751 for PT100 temperature sensor 
Nota: intervallo di misura [70, 350]°K
"""
import numpy as np
from scipy.interpolate import interp1d

class PT100TempSensor:
	
	# Importazione della tabella della curva sensore DIN IEC 751 e creazione dell'interpolatore
	def __init__(self):
		table = np.load('pt100_calibration_table.npz')
		R = table['R']
		T = table['T']
		self.interp = interp1d(R, T, kind='cubic')

	# Interpolazione della tabella 
	# arg: resistenza in ohm (min: , max: )
	def res_to_temp(self, r):
		if(r < 17.1564 or r > 129.6942):
			print("Value out of range:", r)
			pass
		else:
			return self.interp(r)

	# Calcolo tramite formula (deprecato)
	def res_to_temp_formula(self, r):
		return 28.47022 + 2.47285*r
		
    





