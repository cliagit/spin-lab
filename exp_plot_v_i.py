#!/usr/bin/env python3

'''
Plotting experiment data
'''
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import easygui as eg

# Stile della finestra dei grafici
# plt.style.use('dark_background')

file_data = eg.fileopenbox(msg="Browse data", title=None, default='/home/spin/Esperimenti/*.npz',
                           filetypes=["*.npz"], multiple=True)
index = 0
for file in file_data:
    try:
        # Visualizzazione della descrizione dell'esperimento
        with open(file.replace('.npz',''), "r", encoding='utf-8') as file_desc:
            text = file_desc.read()
            print(text)
    except FileNotFoundError:
        print(f"Description of {file} not found.")
    # Caricamento dei dati
    data=np.load(file, allow_pickle=True)
    try:
        if index == 0:
            DT = data['datetime']
            V = data['voltage']
            R = data['resistance']
            I = data['current_source']
            J = data['current_density']
            E = data['electric_field']
            RHO = data['resistivity']
        else:
            DT = np.append(DT, data['datetime'], axis=0)
            V = np.append(V, data['voltage'], axis=0)
            R = np.append(R, data['resistance'], axis=0)
            I = np.append(I, data['current_source'], axis=0)
            J = np.append(J, data['current_density'], axis=0)
            E = np.append(E, data['electric_field'], axis=0)
            RHO = np.append(RHO, data['resistivity'], axis=0)
        index += 1
    except KeyError:
        pass


# Correnti in mA
J = J * 1000
I = I * 1000
unit_current = "mA"

## Grafici 
fig, [ax, ax1] = plt.subplots(2,1)
try:
    ax.plot(I, V, ".")
    # Annotate Start point
    ax.annotate("Start",
        xy=(I[0], V[0]), xycoords='data', color="green")

    # Annotate End point
    # ax.plot(I[-1], V[-1], "o", color="red")
    ax.annotate("End",
        xy=(I[-1], V[-1]), xycoords='data', color="red")
    ax.set(xlabel=unit_current, ylabel='V', title=f"V vs I") #, yscale='log', xscale='log')
    ax.grid()

    ax1.plot(I, R, ".")
    # Annotate Start point
    ax1.annotate("Start",
        xy=(I[0], R[0]), xycoords='data', color="green")

    # Annotate End point
    ax1.annotate("End",
       xy=(I[-1], R[-1]), xycoords='data', color="red")
    ax1.set(xlabel=unit_current, ylabel='Ohm', title=f"R vs I")
    #, yscale='log', xscale='log')
    ax1.grid()
except NameError:
    pass
plt.show()
