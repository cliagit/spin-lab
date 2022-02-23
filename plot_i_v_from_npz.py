import sys
import numpy as np
from matplotlib import pyplot as plt
if len(sys.argv) == 0:
    sys.exit(2)

# Caricamento del file in input
VIData = np.load(sys.argv[1])
V = VIData['V']
I = VIData['I']
maxV = np.max(V)
maxVIndex = np.argmax(V)
# Grafici
title=f'\nI=[{np.min(I):3.4f},{np.max(I):3.4f}] Vmax={maxV:3.4f} at I={I[maxVIndex]:3.4f} samples {V.size}'

fig, [ax, ax1, ax2] = plt.subplots(3,1)
#fig, [ax, ax1] = plt.subplots(2,1)
ax.plot(V, I)

ax1.plot(I,V)
ax1.plot(I[maxVIndex], V[maxVIndex], marker="o")

ax2.plot(I,V/I)

ax.set(ylabel='current (A)', xlabel='voltage (V)', title=sys.argv[1] + title, yscale='log', xscale='log')
ax1.set(xlabel='current (A)', ylabel='voltage (V)', yscale='log', xscale='log')
ax2.set(xlabel='current (A)', ylabel='R (Ohm)', xscale='log')

ax.grid()
ax1.grid()
ax2.grid()
plt.figtext(0.8,0.2, "pippo", c="black", fontsize='x-large')
plt.show()

answer = input("Save figure? [y/N]")
if answer.upper() in ["Y", "YES"]:
    fig.savefig(title.replace(" ", "_") + ".png")
