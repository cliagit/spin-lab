#!/usr/bin/env python3

'''
Read all the data of the experiments and annotate them if oscillations are detected
'''
import os
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import signal
from datetime import datetime


CURRENT_UNIT = "A"
DIR_ESPERIMENTI = "/home/spin/Esperimenti"
DIR_ANALISI = "/Analisi"

# Lettura csv dei esperimenti con oscillazioni
df_osc = pd.read_csv(DIR_ESPERIMENTI + DIR_ANALISI + '/oscillations_analysis.csv')

experiment_base_dir = ''
names = []
experiment_names = []
# Datetime
start_date = []
end_date = []
# Dimensioni del campione
thickness = []
area = []
# Temperatura
minT = []
avgT = []
maxT = []
# Densità di corrente
minJ = []
avgJ = []
maxJ = []
# Restitività
minRho = []
avgRho = []
maxRho = []
# Campo elettrico
minE = []
avgE = []
maxE = []

oscillations = []
oscillations_values = []

# Scansione delle cartelle degli esperimenti
for root, dirs, files in os.walk(DIR_ESPERIMENTI):
    for file in files:
        if file.endswith(".npz"):
            data_file = os.path.join(root, file)
            # Caricamento dei dati
            data=np.load(data_file, allow_pickle=True)
            try:
#                E = data['electric_field']
#                peaks, _ = signal.find_peaks(E, prominence=50)
                exp_name = file.replace('.npz','')
                #if not 'square' in exp_name:
                split_path = data_file.split('/')
                #exp_data_dir = '/'.join(split_path[0:-1])
                experiment_base_dir = split_path[4]
                #print(experiment_base_dir, exp_name)
                # Caricamento dei dati
                DT=data['datetime']
                if len(DT) > 0:
                    osc_row = df_osc.loc[df_osc['Experiment'] == exp_name]
                    V=data['voltage']
                    R=data['resistance']
                    T=data['temperature']
                    I=data['current_source']
                    J=data['current_density']
                    E=data['electric_field']
                    RHO=data['resistivity']
                    names.append(experiment_base_dir)
                    experiment_names.append(exp_name)
                    thickness.append(V[0]/E[0])
                    area.append(I[0]/J[0])
                    start_date.append(DT[0])
                    end_date.append(DT[-1])
                    if len(osc_row['Experiment']) > 0:
                        #print(osc_row['Min Temperature [K]'].values[0])
                        minT.append(osc_row['Min Temperature [K]'].values[0])
                        avgT.append(osc_row['Avg Temperature [K]'].values[0])
                        maxT.append(osc_row['Max Temperature [K]'].values[0])
                        minJ.append(osc_row['Min Current [A/cm2]'].values[0])
                        avgJ.append(osc_row['Avg Current [A/cm2]'].values[0])
                        maxJ.append(osc_row['Max Current [A/cm2]'].values[0])
                        minE.append(osc_row['Min Electrical Field [V/cm]'].values[0])
                        avgE.append(osc_row['Avg Electrical Field [V/cm]'].values[0])
                        maxE.append(osc_row['Max Electrical Field [V/cm]'].values[0])
                        minRho.append(osc_row['Min Restivity [𝛀 cm]'].values[0])
                        avgRho.append(osc_row['Avg Restivity [𝛀 cm]'].values[0])
                        maxRho.append(osc_row['Max Restivity [𝛀 cm]'].values[0])
                        oscillations.append(True)
                        oscillations_values.append(100)

                    else:
                        minT.append(np.min(T))
                        avgT.append(np.average(T))
                        maxT.append(np.max(T))
                        minJ.append(np.min(J))
                        avgJ.append(np.average(J))
                        maxJ.append(np.max(J))
                        minE.append(np.min(E))
                        avgE.append(np.average(E))
                        maxE.append(np.max(E))
                        minRho.append(np.min(RHO))
                        avgRho.append(np.average(RHO))
                        maxRho.append(np.max(RHO))
                        oscillations.append(False)
                        oscillations_values.append(0)
                    print(experiment_base_dir, thickness[-1], area[-1], exp_name, DT[0], DT[-1], len(osc_row['Experiment']) > 0)
                    #print(experiment_base_dir, thickness, area, osc_row['Min Temperature [K]'])
            except KeyError:
                #print('error', e)
                pass

save_path = DIR_ESPERIMENTI + DIR_ANALISI + '/experiments_collector'
# Salvataggio dati nel formato numpy
np.savez_compressed(save_path, name=names, thickness=thickness, area=area, experiment=experiment_names, 
minT=minT, avgT=avgT, maxT=maxT,
minJ=minJ, avgJ=avgJ, maxJ=maxJ, 
minRho=minRho, avgRho=avgRho, maxRho=maxRho,
minE=minE, avgE=avgE, maxE=maxE,
oscillations=oscillations)

# Salvataggio dati formato csv
data = pd.DataFrame(np.stack((names, thickness, area, experiment_names,
start_date, end_date,
minT, avgT, maxT,
minJ, avgJ, maxJ, 
minRho, avgRho, maxRho,
minE, avgE, maxE,
oscillations, oscillations_values), axis=-1),
columns=['Name', 'Thickness [cm]', 'Area [cm2]', 'Experiment',
'Start Date', 'End Date', \
'Min Temperature [K]', 'Avg Temperature [K]', 'Max Temperature [K]', \
'Min Current [A/cm2]', 'Avg Current [A/cm2]', 'Max Current [A/cm2]', \
'Min Restivity [𝛀 cm]', 'Avg Restivity [𝛀 cm]', 'Max Restivity [𝛀 cm]', \
'Min Electrical Field [V/cm]', 'Avg Electrical Field [V/cm]', 'Max Electrical Field [V/cm]', \
'Oscillation', 'Oscillation val'])
data.to_csv(save_path + '.csv', index=False)


