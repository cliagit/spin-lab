#!/usr/bin/env python3

# coding: utf-8

# # Electrical characteristic analysis of sample CA12X2

# In[1]:


paths = [
'/home/spin/Esperimenti/CA12X_C5/CA12X_C5_current_from_1e-7_to_10e-7A/CA12X_C5_current_from_1e-7_to_10e-7A-20220412170113',
'/home/spin/Esperimenti/CA12X_C5/CA12X_C5_at_fixed_current_3.5e-7A/CA12X_C5_at_fixed_current_3.5e-7A-20220413144545',
'/home/spin/Esperimenti/CA8_01_A/CA8_01_A_current_from_0.5e-7_to_4e-7A/CA8_01_A_current_from_0.5e-7_to_4e-7A-20220421185114',
'/home/spin/Esperimenti/CA8_01_A/CA8_01_A_current_from_0.5e-6_to_2e-6A_flipped/CA8_01_A_current_from_0.5e-6_to_2e-6A_flipped-20220421110256',
'/home/spin/Esperimenti/CA12X2/CA12X2_current_from_1e-9_to_10e-9A/CA12X2_current_from_1e-9_to_10e-9A-20220315151857',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_10e-9_to_100e-9A/CA12X2_current_from_10e-9_to_100e-9A-20220315151525',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_100e-9_to_200e-9A/CA12X2_current_from_100e-9_to_200e-9A-20220315152213',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_200e-9_to_300e-9A/CA12X2_current_from_200e-9_to_300e-9A-20220315152513',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_1e-6_to_2e-6A/CA12X2_current_from_1e-6_to_2e-6A-20220317143643',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_0.1e-6_to_1.5e-6A/CA12X2_current_from_0.1e-6_to_1.5e-6A-20220317150657',
'/home/spin/Esperimenti/Analisi/CA12X2/CA12X2_current_from_0.1e-6_to_1.0e-6A/CA12X2_current_from_0.1e-6_to_1.0e-6A-20220317151236']

data_path = paths[1]

with open(data_path, "r", encoding='utf-8') as file_desc:
    text = file_desc.read()
    print(text)


# <img src="../CA12X2/Ca12x2_Info/camp_ca12x2.jpg" width=500 />

# ## Diffrattogramma

# ![title](../CA12X2/Ca12x2_Info/Ca_X2_drx.JPG)

# ## Loading experiment data

# In[2]:


# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from datetime import datetime
import sys

plt.rcParams['figure.figsize'] = [20, 6]


# In[3]:

unit_current = "A"

data = np.load(data_path + '.npz', allow_pickle=True)
DT=data['datetime']
V=data['voltage']
R=data['resistance']
T=data['temperature']
I=data['current_source']
J=data['current_density']
E=data['electric_field']
RHO=data['resistivity']
thickness = V/E
area = I/J
if unit_current == 'mA':
    # Density in mA/cm2
    J = J * 1000
    I = I * 1000


# ### Data description

# - DT datetime
# - V voltage measurements in Volts
# - R resistance measurements in Ohm
# - T temperature measurements in °K
# - I current source in Amps
# - J current density in [m]A/cm^2
# - E electric field in V/cm
# - RHO resistivity in Ohm cm

# In[4]:


print(f"Area {area[0]:.4e}cm2\nThickness:{thickness[0]:.4e}cm")



# ### Input source
plt.plot(E)
#plt.show()

# Se non costante analisi della sola prima rampa
if 'current_from' in data_path or 'flipped' in data_path:
    max_index = np.argmax(I)
#    print(max_index)
    DT = DT[0:max_index]
    V = V[0:max_index]
    R = R[0:max_index]
    T = T[0:max_index]
    I = I[0:max_index]
    J = J[0:max_index]
    E = E[0:max_index]
    RHO = RHO[0:max_index]

elif 'square' in data_path:
    print("square")
    V = abs(V)
    R = abs(R)
    I = abs(I)
    J = abs(J)
    E = abs(E)
    RHO = abs(RHO)

#plt.plot(I)
plt.plot(E)
plt.show()
# ### Temperature

diff = np.max(T) - np.min(T)
if diff <= 0.1: 
     print(f"Temperature is constant: {T[0]:.2f}°K")   
elif diff <= 1: 
    print(f"Temperature is quite constant, average value: {np.average(T):.2f}°K difference between min and max {np.max(T) - np.min(T):.2f}°K")
else:
    print(f"Temperature span from {np.min(T):.2f}°K to {np.max(T):.2f}°K")

# ### Input source
if I[0] == I[-1]: 
    print(f"Source is constant: {I[0]:.2e}{unit_current} ({J[0]:.2e}{unit_current}/cm2)")
else:
    print(f"Source span from {np.min(I):.2e}{unit_current} ({np.min(J):.2e}{unit_current}/cm2) to {np.max(I):.2e}{unit_current} ({np.max(J):.2e}{unit_current}/cm2)")


# ## Analysis

# In[7]:

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
ax3.set_ylabel(unit_current+'/cm2', color='g')
ax3.tick_params(axis='y', labelcolor='g')
ax3.plot(DT, J, 'o-', label='J', color='g')
ax1.legend(loc='lower right')
ax2.legend(loc='right')
ax3.legend(loc='upper right')
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
#fig.savefig('myfig.png')
plt.show()

# ### Peaks detection
# Individuazione dei picchi
peaks, _ = signal.find_peaks(E, prominence=50)
if len(peaks) < 6:
    print('No oscillations found') 
    sys.exit(1)
# Larghezza, Ampiezza base, inizio e fine dei picchi
widths, values, start, end = signal.peak_widths(E, peaks, rel_height=1)
#indexes_start = np.rint(start)
#indexes_end = np.rint(end)
istart = peaks[0] #int(min(indexes_start))
iend = peaks[-1] + 1#int(max(indexes_end))

print(J[0:istart])
print(J[iend:-1])
print('istart:', istart, 'iend:', iend)

fig, ax1 = plt.subplots()
ax1.set_xlabel('time')
ax1.set_ylabel('V/cm', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.plot(DT[istart:iend], E[istart:iend], color='b')
ax1.plot(DT[peaks], E[peaks], 'o', c='orange')
ax1.vlines(DT[peaks], values, E[peaks], color='red')

ax2 = ax1.twinx()
ax2.tick_params(axis='y', labelcolor='C2')
ax2.set_ylabel(unit_current+'/cm2', color='C2')
ax2.plot(DT[istart:iend], J[istart:iend], 'o-', label='J', color='C2')

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
#fig.savefig('myfig1.png')
plt.show()

# #### Peaks amplitude
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
print(f'Outliers {outliers}')
 
''' Removing the Outliers '''
diff = np.delete(diff, outliers)
peaks = np.delete(peaks, outliers)
values = np.delete(values, outliers)
print("New peaks: ", peaks)

istart = peaks[0] #int(min(indexes_start))
iend = peaks[-1] + 1#int(max(indexes_end))


fig, ax1 = plt.subplots()
ax1.set_xlabel('time')
ax1.set_ylabel('V/cm', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.plot(DT[istart:iend], E[istart:iend], color='b')
ax1.plot(DT[peaks], E[peaks], 'o', c='orange')
ax1.vlines(DT[peaks], values, E[peaks], color='red')

ax2 = ax1.twinx()
ax2.tick_params(axis='y', labelcolor='C2')
ax2.set_ylabel(unit_current+'/cm2', color='C2')
ax2.plot(DT[istart:iend], J[istart:iend], 'o-', label='J', color='C2')
ax1.grid(True)
ax2.grid(True)
plt.show()

print(f"Minimum amplitude {np.min(diff):.1f} V/cm at {J[np.argmin(diff)]:.2e} {unit_current}/cm2       \nMaximum amplitude {np.max(diff):.1f} at V/cm at {J[np.argmax(diff)]:.2e} {unit_current}/cm2      \nAverage amplitude {np.mean(diff):.1f} V/cm")


# #### Starting and ending point of the peaks

print(f"First peak with value {E[peaks[0]]:.1f} V/cm, {RHO[peaks[0]]:.3e} Ohm cm at {J[peaks[0]]:.2e} {unit_current}/cm2\nLast peak  with value {E[peaks[-1]]:.1f} V/cm, {RHO[peaks[-1]]:.2e} Ohm cm at {J[peaks[-1]]:.2e} {unit_current}/cm2")



# #### Time interval between peaks [ms]

# In[12]:

diff = np.ediff1d(DT[peaks].astype(dtype='datetime64[ms]'))
print(f"Average time interval between peaks {np.mean(diff)}")

fig, ax1 = plt.subplots()
ax1.set_ylabel('ms')
ax1.bar(peaks[1:], diff.astype(int))
ax1.grid(True)
#fig.savefig('myfig3.png')
plt.show()
''' Detection '''
# IQR
Q1 = np.percentile(diff, 25,
                   interpolation = 'midpoint')
 
Q3 = np.percentile(diff, 75,
                   interpolation = 'midpoint')
IQR = Q3 - Q1
 
print("Old Shape: ", diff.shape)
 
# Upper bound
upper = np.where(diff >= (Q3+1.5*IQR))
# Lower bound
lower = np.where(diff <= (Q1-1.5*IQR))
outliers = np.concatenate([upper[0], lower[0]])
print(f'Outliers {outliers}')
 
''' Removing the Outliers '''
diff_filtered = np.delete(diff, outliers)
peaks_filtered = np.delete(peaks, outliers)


print("New Shape: ", diff_filtered.shape)

fig, ax1 = plt.subplots()
ax1.set_ylabel('ms')
ax1.bar(peaks_filtered[1:],diff_filtered.astype(int))
ax1.grid(True)
#fig.savefig('myfig4.png')
plt.show()
# #### Distance between peaks

# In[13]:


#diff = np.ediff1d(J[peaks])
#fig, ax1 = plt.subplots()
#ax1.set_ylabel(unit_current+'/cm2')
#ax1.bar(peaks[1:], diff)
#ax1.grid(True)
#fig.savefig('myfig4.png')

## In[14]:


#print(np.array2string(diff, formatter={'float_kind':lambda diff: "%.3e" % diff}), unit_current+"/cm2")

