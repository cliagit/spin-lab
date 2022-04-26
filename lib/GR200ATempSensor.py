"""
Implementation of calibration curve GR-200A-250 Germanium temperature sensor 
Nota: intervallo di misura [1, 100]°K
"""
from scipy.interpolate import interp1d

class GR200ATempSensor:
	
	# Creazione della tabella di calibrazione T (K),R (ohm)
	def __init__(self):
		R=[3161, 1376, 660.1, 198.9, 54.51, 8.871, 3.811, 2.969]
		T=[1, 1.4, 2.0, 4.2, 10, 40, 77.4, 100]
		self.interp = interp1d(R, T, kind='linear')

	# Interpolazione della tabella 
	# arg: resistenza in ohm (min: , max: )
	def res_to_temp(self, r):
		if(r < 2.969 or r > 3161):
			print("Value out of range:", r, end="\r")
			pass
		else:
			return self.interp(r)

    





