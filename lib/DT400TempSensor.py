''' 
Implementation of standard curve 10 for silicon diode temperaure sensor model Lake Shore DT-400 
'''
import math
import numpy as np
from scipy.interpolate import interp1d

class DT400TempSensor:
	
	# Importazione della tabella della curva sensore e creazione dell'interpolatore
	def __init__(self):
		table_curve10 = np.load('/home/spin/lib/dt400_series_curve10.npz')
		V = table_curve10['V']
		T = table_curve10['T']
		self.interp = interp1d(V, T, kind='cubic')

	# Interpolazione tramite tabella della curva 10
	# arg: voltaggio in volt
	def voltage_to_temp(self, v):
		return self.interp(v)

	# Chebychev fit coefficients as table 1 of datasheet for prog 1 end 2
	# Range 2K to 12k
	zl1 = 1.32412
	zu1 = 1.69812
	A1 = [7.556358, -5.917261, 0.237238, -0.334636, -0.058642, -0.019929, -0.020715, -0.014814, -0.008789, -0.08554]

	# Range 12K to 24.5k
	zl2 = 1.11732
	zu2 = 1.42013
	A2 = [17.304227, -7.894688, 0.453442, 0.002243, 0.158036, -0.193093, 0.155717, -0.085185, 0.078550, -0.018312, 0.039255]

	# Range 24.5K to 100K
	zl3 = 0.923174
	zu3 = 1.13935
	A3 = [71.818025, -53.799888, 1.669931, 2.314228, 1.566635, 0.723026, -0.149503, 0.046976, -0.388555, 0.056889, -0.116823, 0.058580]

	# Range 100K to 475k
	zl4 = 0.079767
	zu4 = 0.999614
	A4 = [287.756797, -194.144823, -3.837903, -1.318325, -0.109120, -0.393265, 0.146911, -0.111192, 0.028877, -0.029286, 0.015619]

	# Interpolazione della curva tramite serie di Chebychev (non precisa)	
	def voltage_to_temp_prog1(self, z):
		if z >= self.zl4 or z <= self.zu4:
			x = ((z - self.zl4) - (self.zu4 - z)) / (self.zu4 - self.zl4) 
			tc = [0] * len(self.A4)
			tc[1] = x
			t=self.A4[0] + self.A4[1]*x
			for i in range(2,len(self.A4)):
				tc[i] = 2*x*tc[i-1]-tc[i-2]
				t = t + self.A4[i]*tc[i]
			
		return t
	# Interpolazione della curva tramite serie di Chebychev con arccos ( non valida con temperature inferiori a 90K)	
	def voltage_to_temp_prog2(self, z):
		if z >= self.zl4 or z <= self.zu4:
			x = ((z - self.zl4) - (self.zu4 - z)) / (self.zu4 - self.zl4) 
			print("x=", x)
			t=0
			for i in range(0,len(self.A4)):
				# print("i=", i)
				t = t + self.A4[i]*math.cos(i*math.acos(x))
			
		return t

    





