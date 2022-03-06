import matplotlib.pyplot as plt
import numpy as np
data=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303151217.npz')
data1=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303152252.npz')
V=np.concatenate((data['voltage'], data1['voltage']))
R=np.concatenate((data['resistance'], data1['resistance']))
T=np.concatenate((data['temperature'], data1['temperature']))
I=np.concatenate((data['current_source'], data1['current_source']))

# xx, yy = np.meshgrid(I, V, sparse=True)
# x1, zz = np.meshgrid(V, T, sparse=True)
rr = np.delete(R,np.where(R > 10000))
vv = np.delete(V,np.where(R > 10000))
tt = np.delete(T,np.where(R > 10000))
ii = np.delete(I,np.where(R > 10000))

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set(xlabel='current (A)', ylabel='Resistance (Ohm)', zlabel='temperature (°K)')
p = ax.scatter(ii, vv, tt, c=tt/np.max(tt), cmap=plt.cm.magma)
fig.colorbar(p)
plt.show()

