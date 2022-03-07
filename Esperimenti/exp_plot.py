import matplotlib.pyplot as plt
import numpy as np
import easygui as eg
file_name = eg.fileopenbox(msg="Browse data", title=None, default='/home/spin/Esperimenti/*.npz', filetypes=["*.npz"], multiple=False)
data=np.load(file_name)
V=data['voltage']
R=data['resistance']
T=data['temperature']
I=data['current_source']

#data1=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303152252.npz')
#V=np.concatenate((data['voltage'], data1['voltage']))
#R=np.concatenate((data['resistance'], data1['resistance']))
#T=np.concatenate((data['temperature'], data1['temperature']))
#I=np.concatenate((data['current_source'], data1['current_source']))

## xx, yy = np.meshgrid(I, V, sparse=True)
## x1, zz = np.meshgrid(V, T, sparse=True)
#rr = np.delete(R,np.where(R > 10000))
#vv = np.delete(V,np.where(R > 10000))
#tt = np.delete(T,np.where(R > 10000))
#ii = np.delete(I,np.where(R > 10000))
answer = eg.buttonbox('Select the plot', 'Plot', ('V-I', 'R-I'))
fig3d = plt.figure()
ax3d = plt.axes(projection='3d')
mappable = plt.cm.ScalarMappable(cmap=plt.cm.turbo)
mappable.set_array(T)
if answer == 'V-I':
    ax3d.set(title='V-I', xlabel='current (A)', ylabel='Voltage (V)', zlabel='temperature (°K)')
    ax3d.scatter(I, V, T, cmap=mappable.cmap, norm=mappable.norm, c=mappable.get_array())
else:
    ax3d.set(title='R-I', xlabel='current (A)', ylabel='Resistance (Ohm)', zlabel='temperature (°K)')
    ax3d.scatter(I, R, T, cmap=mappable.cmap, norm=mappable.norm, c=mappable.get_array())
fig3d.colorbar(mappable)

##fig, [ax, ax1, ax2] = plt.subplots(3,1)
#fig, [ax, ax1] = plt.subplots(2,1)
#ax.plot(I, V)

##ax1.plot(I,V)
##ax1.plot(I[maxVIndex], V[maxVIndex], marker="o")

#ax1.plot(I,R)

#ax.set(ylabel='current (A)', xlabel='voltage (V)', title="Caratteristica V-I", yscale='log', xscale='log')
## ax1.set(xlabel='current (A)', ylabel='voltage (V)', yscale='log', xscale='log')
#ax1.set(xlabel='current (A)', ylabel='R (Ohm)', xscale='log')

#ax.grid()
#ax1.grid()
##ax2.grid()
#plt.show()

plt.show()

