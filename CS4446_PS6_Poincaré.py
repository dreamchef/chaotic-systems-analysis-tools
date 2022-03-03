import numpy as np 
from matplotlib import pyplot as plt
import math
from math import pi as PI

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
#axs2.set_ylim([-0.1,0.1])
axs1.grid(True)
axs2.grid(True)

# integration parameters
h = 0.005
timeRange = 10000

# physical parameters
m = 0.1 # mass      (kg)
l = 0.1 # length    (m)
B = 0.25 # damping
g = 9.8 # gravity   (m/s)
A = 1.1 # drive amplitude   
a = 1.575553553 # drive frequency 

# initial state
IC = [0.01,0]

stateVector = np.array(IC)

def F(stateVector,t):
    acceleration = (A*math.cos(a*t)-B*l*stateVector[1]-m*g*math.sin(stateVector[0]))/(m*l)
    velocity = stateVector[1]#(A*math.cos(a*t)-m*l*acceleration-m*g*math.sin(stateVector[0]))/(B*l)
    return np.array([velocity,acceleration])

def RK4_step(stateVector,t,h):
    k1 = F(stateVector,t)
    k2 = F(stateVector+(h/2)*k1,t+(h/2))
    k3 = F(stateVector+(h/2)*k2,t+(h/2))
    k4 = F(stateVector+h*k3,t+h)

    return stateVector+(h/6)*(k1+2*k2+2*k3+k4)

time = np.arange(0.0, timeRange, h)
thetas = []
omegas = []
timeTrajectory = []

# time-stepping solution
for t in time:
    stateVector = RK4_step(stateVector,t,h)

    thetas.append(stateVector[0]%(2*PI))
    omegas.append(stateVector[1])
    #axs1.plot(stateVector[0],stateVector[1],markersize=1,marker='o',linestyle='',color='blue')
    
    timeTrajectory.append([stateVector[0]%(2*PI),stateVector[1],t])

axs1.plot(thetas,omegas,markersize=0.2,marker='o',linestyle='')

# POINCARE SECTION

poincarePeriod = 2*PI/a
currentPeriod = 0
# natural period of (linearized version of?) the system is 0.64
poincareTime = np.arange(0.0, timeRange-(timeRange%poincarePeriod), poincarePeriod)
currentPoint = 0
point = timeTrajectory[currentPoint]
sectionThetas = []
sectionOmegas = []

for pt in poincareTime:
    while point[2] < pt:
        currentPoint += 1
        point = timeTrajectory[currentPoint]
    sectionThetas.append(point[0])
    sectionOmegas.append(point[1])

lenTransient = 0 #int((len(sectionThetas)/1.5))

print(len(sectionThetas))
print(lenTransient)

axs2.plot(sectionThetas[-1500:-1],sectionOmegas[-1500:-1],markersize=1,marker='o',linestyle='',color='blue')
plt.show()