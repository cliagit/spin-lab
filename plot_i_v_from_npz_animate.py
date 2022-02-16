import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

if len(sys.argv) <= 1:
    print("Input file is required")
    sys.exit(2)

# Caricamento del file in input
VIData = np.load(sys.argv[1])
V = VIData['V']
I = VIData['I']
maxV = np.max(V)
maxVIndex = np.argmax(V)
# Grafici
title=f'\nI=[{np.min(I):3.4f},{np.max(I):3.4f}] Vmax={maxV:3.4f} at I={I[maxVIndex]:3.4f} samples {V.size}'

# fig, [ax, ax1, ax2] = plt.subplots(3,1)
fig, ax = plt.subplots()


ax.grid()

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    # print(i, V[i], I[i])
    plt.plot(V[:i], I[:i], color='green')


anim = animation.FuncAnimation(plt.gcf(), animate, interval=200, blit=False)

plt.show()

#answer = input("Save figure? [y/N]")
#if answer.upper() in ["Y", "YES"]:
#    fig.savefig(title.replace(" ", "_") + ".png")
