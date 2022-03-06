import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 

data=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303151217.npz')
data1=np.load('./CA12X2_current_from_1e-5_to_50e-3A/CA12X2_current_from_1e-5_to_50e-3A-20220303152252.npz')
V=np.concatenate((data['voltage'], data1['voltage']))
R=np.concatenate((data['resistance'], data1['resistance']))
T=np.concatenate((data['temperature'], data1['temperature']))
I=np.concatenate((data['current_source'], data1['current_source']))
   
# creating a blank window
# for the animation 
fig = plt.figure() 
#axis = plt.axes(xlim =(0, 50e-3), ylim =(0, 50)) 
ax = plt.axes(xlim =(0, 50e-3), ylim =(0, 50), zlim=(0,300), projection='3d')
ax.set(xlabel='current (A)', ylabel='voltage (V)', zlabel='temperature (°K)') #, yscale='log', xscale='log')
line, = ax.plot([], [], [], 'o') 
   
# what will our line dataset
# contain?
def init(): 
    line.set_data([], []) 
    line.set_3d_properties([])
    return line, 
   
# initializing empty values
# for x and y co-ordinates
xdata, ydata, zdata = [], [], [] 
   
# animation function 
def animate(i): 
         
    # appending values to the previously 
    # empty x and y data holders 
    if i < len(I):
        xdata.append(I[i]) 
        ydata.append(V[i]) 
        zdata.append(T[i]) 
        line.set_data(xdata, ydata)
        line.set_3d_properties(zdata)
      
    return line,
   
# calling the animation function     
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                               frames = 500, interval = 200, blit = True) 
plt.show()
