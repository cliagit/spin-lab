import matplotlib.pyplot as plt
import numpy as np
data=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303151217.npz')
V=data['voltage']
R=data['resistance']
T=data['temperature']
I=data['current_source']
ax = plt.axes(projection='3d')
ax.set(xlabel='current (A)', ylabel='voltage (V)', zlabel='temperature (°K)') #, yscale='log', xscale='log')
ax.scatter3D(I, V, T)
plt.show()


