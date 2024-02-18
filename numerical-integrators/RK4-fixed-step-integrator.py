import numpy as np 
from matplotlib import pyplot as plt
import math
from math import pi as PI

fig = plt.figure()
fig.set_size_inches(21,10)
plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)
#plt.gca().set_aspect('equal', adjustable='box')
axs = fig.add_subplot()
axs.set_ylabel('Angular Velocity (rad/s)')
axs.set_xlabel('Angle (radians)')
axs.set_title('State-Space Trajectory')
#axs.set_xlim([-20,20])
#axs.set_ylim([-65,65])
plt.grid(True)

# integration parameters
h = 0.005

# physical parameters
m = 0.1 # mass      (kg)
l = 0.1 # length    (m)
B = 0.25 # damping
g = 9.8 # gravity   (m/s)
A = 1 # drive amplitude   
a = 1.58 # drive frequency 

ICs = [[0.01,0]]

        # [0.05,50],       [0.1,50],        [1,50],          [5,30],
        # [2*PI+0.05,50], [2*PI+0.1,50],  [2*PI+1,50],    [2*PI+2,35],
        # [4*PI+0.05,50], [4*PI+0.1,50],  [4*PI+1,10],    [4*PI+2,50],
        # #[4*PI+0.05,100], [4*PI+0.1,100],  [4*PI+1,100],    [4*PI+2,100],

        # [0.05,-50],       [0.1,-50],        [1,-50],          [2,-30],
        # [2*PI+0.05,-50], [2*PI+0.1,-50],  [2*PI+1,-50],    [2*PI+2,-35],
        # [4*PI+0.05,-50], [4*PI+0.1,-50],  [4*PI+1,-10],    [4*PI+2,-50],
        # #[4*PI+0.05,-100], [4*PI+0.1,-100],  [4*PI+1,-100],    [4*PI+2,-100],


        # [0.05,-50],       [0.1,-50],        [1,-50],          [2,-30],
        # [10*PI+0.05,-50], [10*PI+0.1,-50],  [10*PI+1,-50],    [10*PI+2,-35],
        # [15*PI+0.05,-50], [15*PI+0.1,-50],  [15*PI+1,-10],    [15*PI+2,-50],
        # #[20*PI+0.05,-100], [20*PI+0.1,-100],  [20*PI+1,-100],   [20*PI+2,-100],

        # [0.05,50],       [0.1,50],        [1,50],          [2,30],
        # [-10*PI+0.05,50], [-10*PI+0.1,50],  [-10*PI+1,50],    [-10*PI+2,35],
        # [-15*PI+0.05,50], [-15*PI+0.1,50],  [-15*PI+1,10],    [-15*PI+2,50]]
        # #[-20*PI+0.05,100], [-20*PI+0.1,100],  [-20*PI+1,100],   [-20*PI+2,100]]

for IC in ICs:

    # initial state
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

    time = np.arange(0.0, 500, h)
    thetas = []
    omegas = []

    # time-stepping solution
    for t in time:
        stateVector = RK4_step(stateVector,t,h)

        thetas.append(stateVector[0])
        omegas.append(stateVector[1])

    plt.plot(thetas,omegas,markersize=1,marker='o',linestyle='')

plt.show()