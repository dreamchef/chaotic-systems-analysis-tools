from time import time
import numpy as np 
from matplotlib import pyplot as plt
import math
from math import pi as PI
import matplotlib.ticker as tck

fig = plt.figure()
fig.set_size_inches(21,10)
#plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)
#plt.gca().set_aspect('equal', adjustable='box')
axs1 = fig.add_subplot(221)
axs1.set_ylabel('Angular Velocity (rad/s)')
axs1.set_xlabel('Angle (radians)')
axs1.set_title('State-Space Trajectory')
axs2 = fig.add_subplot(222)
axs2.set_ylabel('Angular Velocity (rad/s)')
axs2.set_xlabel('Angle (radians)')
axs2.set_title('Temporal Poincaré Section')
#axs2.set_xlim([-0.011,0.011])
#axs2.set_ylim([-0.11,0.11])
axs1.grid(True)
axs2.grid(True)

lines = 10
time = [] # unit: sec
angle = [] # unit: deg
velocity = [0] # unit: deg/sec, note: unknown at index 0
sampleRate = 100 # unit: data point

with open('ps8data/data1') as file:
    for line in file:
        angle.append(float(line.split()[0]))
        time.append(float(line.split()[1]))
        
print("--data imported--")
for i in range(sampleRate,len(time),sampleRate):
    #print("data point",i,"\n time:",time[i],"\n angle",angle[i])
    velocity.append(
        (angle[i]-angle[i-sampleRate])
        /
        (time[i]-time[i-sampleRate])
    )
    print(velocity[-1])
    
