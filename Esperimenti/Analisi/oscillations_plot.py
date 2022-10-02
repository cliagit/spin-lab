import matplotlib.pyplot as plt
import numpy as np
data=np.load('./oscillations_analysis.npz', allow_pickle=True)

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
#selected_name = names[2]
# Initialize figure and axis
fig, ax = plt.subplots(figsize=(32, 18))
fig1, ax1 = plt.subplots(figsize=(32, 18))
fig2, ax2 = plt.subplots(figsize=(32, 18))
fig3, ax3 = plt.subplots(figsize=(32, 18))

# Selettore esperimenti con corrente fissa (True) False per tutti
FIXED_SOURCE = False

if FIXED_SOURCE:
    file_name_suffix = '_fixed_source'
    names = ['CA8_01_A','CA12X_C5', 'CA12X2_C1']
else:
    file_name_suffix = ''
    names = ['CA12X2', 'CA12_01_A', 'CA8_01_A','CA12X_C5', 'CA12X2_C1']

for (selected_name, color) in zip(names, colors):
    #avg
    name = data['name']
    fixed_source = data['fixed_source']
    avgJ = data['avgJ'] #abs(data['avgJ'])
    avgT = data['avgT']
    avgRho = data['avgRho']
    avg_osc_amp = data['avg_osc_amp_e']
    avg_osc_width = data['avg_osc_width_e']
    #Select
    if FIXED_SOURCE:
        avgJ = avgJ[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        avgT = avgT[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        avgRho = avgRho[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        avg_osc_amp = avg_osc_amp[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        avg_osc_width = avg_osc_width[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
    else:
        avgJ = avgJ[np.where(name == selected_name)]
        avgT = avgT[np.where(name == selected_name)]
        avgRho = avgRho[np.where(name == selected_name)]
        avg_osc_amp = avg_osc_amp[np.where(name == selected_name)]
        avg_osc_width = avg_osc_width[np.where(name == selected_name)]

    avgJ = avgJ[np.where(avgJ >= 0)]
    avgT = avgT[np.where(avgJ >= 0)]
    avgRho = avgRho[np.where(avgJ >= 0)]
    avg_osc_amp = avg_osc_amp[np.where(avgJ >= 0)]
    avg_osc_width = avg_osc_width[np.where(avgJ >= 0)]

    # Ordinamento per temperature crescenti
    avgTSortedIndex = np.argsort(avgT)
    avgJ = avgJ[avgTSortedIndex]
    avgT= avgT[avgTSortedIndex]
    avgRho= avgRho[avgTSortedIndex]
    avg_osc_amp = avg_osc_amp[avgTSortedIndex]
    avg_osc_width = avg_osc_width[avgTSortedIndex]

    #min
    minJ = data['minJ'] #abs(data['minJ'])
    minT = data['minT']
    minRho = data['minRho']
    min_osc_amp = data['min_osc_amp_e']
    min_osc_width = data['min_osc_width_e']
    #Select
    if FIXED_SOURCE:
        minJ = minJ[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        minT = minT[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        minRho = minRho[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        min_osc_amp = min_osc_amp[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        min_osc_width = min_osc_width[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
    else:
        minJ = minJ[np.where(name == selected_name)]
        minT = minT[np.where(name == selected_name)]
        minRho = minRho[np.where(name == selected_name)]
        min_osc_amp = min_osc_amp[np.where(name == selected_name)]
        min_osc_width = min_osc_width[np.where(name == selected_name)]

    minJ = minJ[np.where(minJ >= 0)]
    minT = minT[np.where(minJ >= 0)]
    minRho = minRho[np.where(minJ >= 0)]
    min_osc_amp = min_osc_amp[np.where(minJ >= 0)]
    min_osc_width = min_osc_width[np.where(minJ >= 0)]
    
    # Ordinamento per temperature crescenti
    minJ = minJ[avgTSortedIndex]
    minT= minT[avgTSortedIndex]
    minRho= minRho[avgTSortedIndex]
    min_osc_amp = min_osc_amp[avgTSortedIndex]
    min_osc_width = min_osc_width[avgTSortedIndex]
    minT_min = np.min(minT)
    minJ_min = np.min(minJ)

#    print(f"Min T for {selected_name}: {np.min(minT)}")
#    print(f"Min J for {selected_name}: {np.min(minJ)}")

    #max
    maxJ = data['maxJ'] #abs(data['maxJ'])
    maxT = data['maxT']
    maxRho = data['maxRho']
    max_osc_amp = data['max_osc_amp_e']
    max_osc_width = data['max_osc_width_e']
    #Select
    if FIXED_SOURCE:
        maxJ = maxJ[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        maxT = maxT[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        maxRho = maxRho[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        max_osc_amp = max_osc_amp[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
        max_osc_width = max_osc_width[np.where((name == selected_name) & (fixed_source == FIXED_SOURCE))]
    else:
        maxJ = maxJ[np.where(name == selected_name)]
        maxT = maxT[np.where(name == selected_name)]
        maxRho = maxRho[np.where(name == selected_name)]
        max_osc_amp = max_osc_amp[np.where(name == selected_name)]
        max_osc_width = max_osc_width[np.where(name == selected_name)]


    maxJ = maxJ[np.where(maxJ >= 0)]
    maxT = maxT[np.where(maxJ >= 0)]
    maxRho = maxRho[np.where(maxJ >= 0)]
    max_osc_amp = max_osc_amp[np.where(maxJ >= 0)]
    max_osc_width = max_osc_width[np.where(maxJ >= 0)]
    
    # Ordinamento per temperature crescenti
    maxJ = maxJ[avgTSortedIndex]
    maxT= maxT[avgTSortedIndex]
    maxRho= maxRho[avgTSortedIndex]
    max_osc_amp = max_osc_amp[avgTSortedIndex]
    max_osc_width = max_osc_width[avgTSortedIndex]
    maxT_max = np.max(maxT)
    maxJ_max = np.max(maxJ)

#    print(f"Max T for {selected_name}: {np.max(maxT)}")
#    print(f"Max J for {selected_name}: {np.max(maxJ)}")

    # Periodo medio delle oscillazioni del campo elettrico
    scatter = ax1.scatter(avgT, avgJ, s=avg_osc_width/10, alpha=0.4, color="{}".format(color),
    label=selected_name + f" Min {int(np.min(avg_osc_width))}ms Max {int(np.max(avg_osc_width))}ms")
    ax1.set(ylabel='J [A/cm2]', xlabel='Temperature [°K]', yscale='log')
    ax1.set_title(f"Periodo medio delle oscillazioni")
    ax1.grid(True)

    # Ampiezza media delle oscillazioni del campo elettrico
    ax2.scatter(avgT, avgJ, s=avg_osc_amp, alpha=0.4, color="{}".format(color),
    label=selected_name + f" Min {int(np.min(avg_osc_amp))}V/cm Max {int(np.max(avg_osc_amp))}V/cm")
    ax2.set(ylabel='J [A/cm2]', xlabel='Temperature [°K]', yscale='log')
    ax2.set_title(f"Ampiezza media delle oscillazioni del campo elettrico")
    ax2.grid(True)

    # Resistività media
#    ax3.scatter(avgT, avgJ, s=avgRho/100000, alpha=0.4, color="{}".format(color),
#    label=selected_name + f" Min {int(np.min(avgRho)):.2e}Ohm cm Max {int(np.max(avgRho)):.2e}Ohm cm")
#    ax3.set(ylabel='J [A/cm2]', xlabel='Temperature [°K]', yscale='log')
#    ax3.set_title(f"Restitività media")
#    ax3.grid(True)


    if selected_name == names[0]:
        hide_legend = ''
    else:
        hide_legend = '_'
    
    # Plot lines
#    ax.plot(avgT, minJ, '.', color="{}".format(color), label=hide_legend + 'Min J')
#    ax.plot(avgT, maxJ, 'x', color="{}".format(color), label=hide_legend + 'Max J')
    ax.plot(avgT, avgJ, 'o', color="{}".format(color), label=hide_legend + 'Avg J')
    
    ax.hlines(minJ_min, minT_min, maxT_max, color="{}".format(color), label=selected_name)
    ax.hlines(maxJ_max, minT_min, maxT_max, color="{}".format(color))
    ax.vlines(minT_min, minJ_min, maxJ_max, color="{}".format(color))
    ax.vlines(maxT_max, minJ_min, maxJ_max, color="{}".format(color))
    ax.set(ylabel='J [A/cm2]', xlabel='Temperature [°K]', yscale='log')
    ax.set_title("Intervalli di corrente e temperatura che delimitano la zona di oscillazione del \
cristallo\nCorrente e temperatura media degli esperimenti con oscillazioni")
    ax.grid(True)
    
    ax.fill(([minT_min, minT_min, maxT_max, maxT_max, minT_min]), 
            ([minJ_min, maxJ_max, maxJ_max, minJ_min, minJ_min]), 
            color="{}".format(color), alpha=0.10)

ax.legend();
fig.savefig('oscillations_range' + file_name_suffix + '.png')
plt.close(fig)

ax1.legend();
fig1.savefig('oscillations_width' + file_name_suffix + '.png')
plt.close(fig1)

ax2.legend();
fig2.savefig('oscillations_amplitude' + file_name_suffix + '.png')
plt.close(fig2)

#ax3.legend();
#fig3.savefig('oscillations_resistivity' + file_name_suffix + '.png')
#plt.close(fig3)

#plt.show()