#!/usr/bin/env python3

'''
Plotting 3D
'''
import matplotlib.pyplot as plt
import numpy as np
import easygui as eg

# Stile della finestra dei grafici
# plt.style.use('dark_background')

file_name = eg.fileopenbox(msg="Browse data", title=None, default='/home/spin/Esperimenti/*.npz', filetypes=["*.npz"], multiple=False)
data=np.load(file_name)
try:
    V=data['voltage']
    R=data['resistance']
    T=data['temperature']
    I=data['current_source']
    J=data['current_density']
    E=data['electric_field']
    RHO=data['resistivity']
except KeyError:
    pass
# answer = eg.choicebox('Select the plot', 'Plot', ["V vs I and Temperature", "RHO vs I and Temperature", "V vs I",  "RHO vs I"])

if np.max(T) - np.min(T) > 6:
    mappable = plt.cm.ScalarMappable(cmap=plt.cm.turbo)
    mappable.set_array(T)

    fig3d_a = plt.figure()
    ax3d_a = plt.axes(projection='3d')
    fig3d_a.colorbar(mappable)

    fig3d_b = plt.figure()
    ax3d_b = plt.axes(projection='3d')
    fig3d_b.colorbar(mappable)

    fig3d_c = plt.figure()
    ax3d_c = plt.axes(projection='3d')
    fig3d_c.colorbar(mappable)


#if answer == "V vs I and Temperature":
    ax3d_a.set(title="V vs I and Temperature", xlabel='A', ylabel='V', zlabel='Temperature (°K)')
    ax3d_a.scatter(I, V, T, cmap=mappable.cmap, norm=mappable.norm, c=mappable.get_array())
# elif answer == "Rho vs I and Temperature":
    try:
        ax3d_b.set(title='E vs J and Temperature', xlabel='A/cm2', ylabel='V cm', zlabel='Temperature (°K)')
        ax3d_b.scatter(J, E, T, cmap=mappable.cmap, norm=mappable.norm, c=mappable.get_array())

        ax3d_c.set(title='Rho vs J and Temperature', xlabel='A/cm2', ylabel='Ohm cm', zlabel='Temperature (°K)')
        ax3d_c.scatter(J, RHO, T, cmap=mappable.cmap, norm=mappable.norm, c=mappable.get_array())

    except NameError:
        pass
#else:
#    pass
else:
    fig, [ax, ax1] = plt.subplots(2,1)
    ax.plot(I, V, ".")
    ax.set(xlabel='A', ylabel='V', title="V-I Characteristics", yscale='log', xscale='log')
    ax.grid()

    try:
        ax1.plot(J, RHO, ".")
        ax1.set(xlabel='A/cm2', ylabel='Ohm cm', title="Resistivity vs J", yscale='log', xscale='log')
        ax1.grid()
    except NameError:
        pass


plt.show()


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

