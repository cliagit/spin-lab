#!/usr/bin/env python3

'''
Find ocillations in the data of the experiments
Read all the data of the experiments and annotate them if oscillations are detected
'''
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import signal
#from datetime import datetime

# Stile della finestra dei grafici
# plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [20, 6]

CURRENT_UNIT = "A"
DIR_ESPERIMENTI = "/home/spin/Esperimenti"
DIR_ANALISI = "/Analisi"

experiment_base_dir = ''
names = []
experiment_names = []
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

# Ampiezza delle oscillazioni del campo elettrico
min_osc_amp_e = []
avg_osc_amp_e = []
max_osc_amp_e = []
# Periodo delle oscillazioni del campo elettrico
min_osc_width_e = []
avg_osc_width_e = []
max_osc_width_e = []

fixed_source = []
def oscillations_analysis(experiment_name, experiment_data):
    '''
    Ricerca e Analisi delle oscillazioni.
    '''
    description = ''

    try:

        # Caricamento dei dati
        DT=experiment_data['datetime']
        V=experiment_data['voltage']
        R=experiment_data['resistance']
        T=experiment_data['temperature']
        I=experiment_data['current_source']
        J=experiment_data['current_density']
        E=experiment_data['electric_field']
        RHO=experiment_data['resistivity']
#        if CURRENT_UNIT == 'mA':
#            # Density in mA/cm2
#            J = J * 1000
#            I = I * 1000
        # Se non costante analisi della sola prima rampa
        if 'current_from' in experiment_name or 'flipped' in experiment_name:
            max_index = np.argmax(I)
            DT = DT[0:max_index]
            V = V[0:max_index]
            R = R[0:max_index]
            T = T[0:max_index]
            I = I[0:max_index]
            J = J[0:max_index]
            E = E[0:max_index]
            RHO = RHO[0:max_index]
        elif 'square' in experiment_name:
            V = abs(V)
            R = abs(R)
            I = abs(I)
            J = abs(J)
            E = abs(E)
            RHO = abs(RHO)
        # ## Analysis
        # ### Peaks detection
        # Individuazione dei picchi
        peaks, _ = signal.find_peaks(E, prominence=50)
        if len(peaks) < 6:
            print('No oscillations found')
            return False

        # Creazione della cartella analisi dell'esperimento selezionato
        analisi_path = DIR_ESPERIMENTI + '/' + experiment_base_dir + DIR_ANALISI
        analisi_symlink = DIR_ESPERIMENTI + DIR_ANALISI + '/' + experiment_base_dir
#        print(analisi_path + '/' + experiment_name)
#        print(analisi_symlink)
        if not os.path.exists(analisi_path):
            os.mkdir(analisi_path)
        # Link simbolico per facilitare l'accesso
        if not os.path.exists(analisi_symlink):
            os.symlink(analisi_path, analisi_symlink)

        thickness = V/E
        area = I/J
        description += f"Area {area[0]:.4e}cm2\nThickness:{thickness[0]:.4e}cm\n\n"

        # Larghezza, Ampiezza base, inizio e fine dei picchi
        widths, values, start, end = signal.peak_widths(E, peaks, rel_height=1)

        # #### Peaks amplitude outliers filter
        diff = E[peaks]-values
        # IQR
        Q1 = np.percentile(diff, 25,
                           interpolation = 'midpoint')
         
        Q3 = np.percentile(diff, 75,
                           interpolation = 'midpoint')
        IQR = Q3 - Q1
         
        #print("Old Shape: ", diff.shape)
         
        # Upper bound
        upper = np.where(diff >= (Q3+1.5*IQR))
        # Lower bound
        lower = np.where(diff <= (Q1-1.5*IQR))
        outliers = np.concatenate([upper[0], lower[0]])
        #print(f'Peaks Outliers {outliers}')
         
        ''' Removing the Outliers '''
        diff = np.delete(diff, outliers)
        peaks = np.delete(peaks, outliers)
        values = np.delete(values, outliers)
        #print("New peaks: ", peaks)

        istart = peaks[0] 
        iend = peaks[-1] + 1
        
        # Grafico completo
        fig, ax1 = plt.subplots()
        ax1.set_title("Electrical field, Resistivity and Current Density")
        ax1.set_xlabel('time')
        ax1.set_ylabel('Ohm cm', color='m')
        ax1.tick_params(axis='y', labelcolor='m')
        ax1.plot(DT, RHO, '.-', color='m', label='RHO')
        ax2 = ax1.twinx()
        ax2.set_ylabel('V/cm', color='b')
        ax2.tick_params(axis='y', labelcolor='b')
        ax2.plot(DT, E, 'v-', color='b', label='E')
        ax1.legend(loc='upper right')
        ax2.legend(loc='upper left')
        ax3 = ax1.twinx()
        ax3.set_ylabel(CURRENT_UNIT+'/cm2', color='g')
        ax3.tick_params(axis='y', labelcolor='g')
        ax3.plot(DT, J, 'o-', label='J', color='g')
        ax1.legend(loc='lower right')
        ax2.legend(loc='right')
        ax3.legend(loc='upper right')
        ax1.grid(True)
        ax2.grid(True)
        ax3.grid(True)
        fig.savefig(analisi_path + '/' + experiment_name + '_graph.png')
        plt.close(fig)

        # Grafico delle oscillazioni
        fig, ax1 = plt.subplots()
        ax1.set_xlabel('time')
        ax1.set_ylabel('V/cm', color='b')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.plot(DT[istart:iend], E[istart:iend], color='b')
        ax1.plot(DT[peaks], E[peaks], 'o', c='orange')
        ax1.vlines(DT[peaks], values, E[peaks], color='red')

        ax2 = ax1.twinx()
        ax2.set_ylabel(CURRENT_UNIT+'/cm2', color='g')
        ax2.tick_params(axis='y', labelcolor='g')
        ax2.plot(DT[istart:iend], J[istart:iend], 'o-', label='J', color='g')

        #ax3 = ax2.twinx()
        #ax3.set_ylabel('°K', color='C3')
        #ax3.tick_params(axis='y', labelcolor='C3')
        #ax3.plot(DT[istart:iend], T[istart:iend], 'o-', label='T', color='C3')

        #plt.plot(DT[indexes_end.astype(int)], E[indexes_end.astype(int)], 'x')
        #plt.hlines(values, DT[indexes_start.astype(int)], DT[indexes_end.astype(int)], color="C3")
        #plt.ylabel('V/cm')
        ax1.grid(True)
        ax2.grid(True)
        #ax3.grid(True)
        fig.savefig(analisi_path + '/' + experiment_name + '_peaks.png')
        plt.close(fig)

        # #### Time interval between peaks [ms]
        diff = np.ediff1d(DT[peaks].astype(dtype='datetime64[ms]'))
        ti_mean = np.mean(diff)
        #description += f"Time interval between peaks:\nMinimum {np.min(diff)}\nAverage {np.mean(diff)}\nMaximum {np.max(diff)}\n"

        ''' Filtraggio dei valori anomali '''
        # IQR
        Q1 = np.percentile(diff, 25,
                           interpolation = 'midpoint')

        Q3 = np.percentile(diff, 75,
                           interpolation = 'midpoint')
        IQR = Q3 - Q1

        # Upper bound
        upper = np.where(diff >= (Q3+1.5*IQR))
        # Lower bound
        lower = np.where(diff <= (Q1-1.5*IQR))
        outliers = np.concatenate([upper[0], lower[0]])
#        print(f'Outliers {outliers}')

        ''' Removing the Outliers '''
        diff_filtered = np.delete(diff, outliers)
        peaks_filtered = np.delete(peaks, outliers)       

        # Grafico periodo delle oscillazioni 
        fig, ax1 = plt.subplots()
        ax1.set_ylabel('ms')
        ax1.bar(peaks_filtered[1:],diff_filtered.astype(int))
        ax1.grid(True)
        fig.savefig(analisi_path + '/' + experiment_name + '_peaks_interval.png')
        plt.close(fig)

        # Temperatura durante la fase oscillatoria
        T = T[istart:iend]
        # ### Temperature
        diff = np.max(T) - np.min(T)
        if diff <= 0.5:
            description += f"Temperature is constant: {T[0]:.2f}°K\n\n"
        elif diff <= 1:
            description += f"Temperature is quite constant, average value: {np.average(T):.2f}°K difference between min and max {np.max(T) - np.min(T):.2f}°K\n\n"
        else:
            description += f"Temperature span from {np.min(T):.2f}°K to {np.max(T):.2f}°K\n\n"

        minT.append(np.min(T))
        avgT.append(np.average(T))
        maxT.append(np.max(T))

        # Corrente e sua densità durante la fase oscillatoria
        I = I[istart:iend]
        J = J[istart:iend]
        # ### Input source
        if I[0] == I[-1]:
            description += f"Source is constant: {I[0]:.3e}{CURRENT_UNIT} ({J[0]:.3e}{CURRENT_UNIT}/cm2)\n\n"
            fixed_source.append(True)
        else:
            description += f"Source span from {np.min(I):.3e}{CURRENT_UNIT} ({np.min(J):.3e}{CURRENT_UNIT}/cm2) to {np.max(I):.3e}{CURRENT_UNIT} ({np.max(J):.3e}{CURRENT_UNIT}/cm2)\n\n"
            fixed_source.append(False)

        minJ.append(np.min(J))
        avgJ.append(np.average(J))
        maxJ.append(np.max(J))
        
        # Resistività durante la fase oscillatoria
        RHO = RHO[istart:iend]
        minRho.append(np.min(RHO))
        avgRho.append(np.average(RHO))
        maxRho.append(np.max(RHO))
        
        # Campo elettrico durante la fase oscillatoria
        E_osc = E[istart:iend]
        minE.append(np.min(E_osc))
        avgE.append(np.average(E_osc))
        maxE.append(np.max(E_osc))

        
        # #### Oscillations amplitude
        diff = E[peaks]-values
        description += f"Minimum amplitude {np.min(diff):.1f} V/cm at {J[np.argmin(diff)]:.2e} {CURRENT_UNIT}/cm2\nMaximum amplitude {np.max(diff):.1f} at V/cm at {J[np.argmax(diff)]:.2e} {CURRENT_UNIT}/cm2\nAverage amplitude {np.mean(diff):.1f} V/cm\n\n"

        # Ampiezza delle oscillazioni del campo elettrico
        min_osc_amp_e.append(np.min(diff))
        avg_osc_amp_e.append(np.average(diff))
        max_osc_amp_e.append(np.max(diff))

        # Periodo delle oscillazioni
        description += f"Time interval between peaks:\nMinimum {np.min(diff_filtered)}\nAverage {np.mean(diff_filtered)}\nMaximum {np.max(diff_filtered)}\n"
        min_osc_width_e.append(np.min(diff_filtered.astype(int)))
        avg_osc_width_e.append(np.average(diff_filtered.astype(int)))
        max_osc_width_e.append(np.max(diff_filtered.astype(int)))

        names.append(experiment_base_dir)
        experiment_names.append(experiment_name)
        
        # Inserire parte in cui non sono presenti le oscillazioni
        
        
        # Salvataggio della descrizione
        with open(analisi_path + '/' + experiment_name, "w", encoding='utf-8') as file_desc:
            file_desc.write(description)

        return True

    except OSError as error:
        print(error)
#    except FileNotFoundError:
#        #print(f"Description of {file_desc} not found.")
#        print("Errore")


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
                print(exp_name)
                oscillations_analysis(exp_name, data)
            except KeyError:
                pass

save_path = DIR_ESPERIMENTI + DIR_ANALISI + '/oscillations_analysis'
# Salvataggio dati nel formato numpy
np.savez_compressed(save_path, name=names, experiment=experiment_names, 
minT=minT, avgT=avgT, maxT=maxT,
minJ=minJ, avgJ=avgJ, maxJ=maxJ, 
minRho=minRho, avgRho=avgRho, maxRho=maxRho,
minE=minE, avgE=avgE, maxE=maxE,
min_osc_amp_e=min_osc_amp_e, avg_osc_amp_e=avg_osc_amp_e, max_osc_amp_e=max_osc_amp_e, 
min_osc_width_e=min_osc_width_e, avg_osc_width_e=avg_osc_width_e, max_osc_width_e=max_osc_width_e,
fixed_source=fixed_source)

# Salvataggio dati formato csv
data = pd.DataFrame(np.stack((names, experiment_names,
minT, avgT, maxT,
minJ, avgJ, maxJ, 
minRho, avgRho, maxRho,
minE, avgE, maxE,
min_osc_amp_e, avg_osc_amp_e, max_osc_amp_e, 
min_osc_width_e, avg_osc_width_e, max_osc_width_e,
fixed_source), axis=-1),
columns=['Name', 'Experiment',
'Min Temperature [K]', 'Avg Temperature [K]', 'Max Temperature [K]', \
'Min Current [A/cm2]', 'Avg Current [A/cm2]', 'Max Current [A/cm2]', \
'Min Restivity [𝛀 cm]', 'Avg Restivity [𝛀 cm]', 'Max Restivity [𝛀 cm]', \
'Min Electrical Field [V/cm]', 'Avg Electrical Field [V/cm]', 'Max Electrical Field [V/cm]', \
'Min Osc Amplitude [V/cm]', 'Avg Osc Amplitude [V/cm]', 'Max Osc Amplitude [V/cm]', \
'Min Osc Period [ms]', 'Avg Osc Period [ms]', 'Max Osc Period [ms]', \
'Fixed Source'])
data.to_csv(save_path + '.csv', index=False)


