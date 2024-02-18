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

# physical parameters
m = 0.1 # mass      (kg)
l = 0.1 # length    (m)
B = 0.0 # damping
g = 9.8 # gravity   (m/s)
A = 0   # drive amplitude   
a = 0  # drive frequency 

ICs = [ [0,1]]

# integration parameters
tolerance = 0.00001

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

thetas = []
omegas = []

for IC in ICs:

	stateVector = IC

    # initial state
	timeRange = 100
	t = 0
	h = 0.005

    # time-stepping solution
	while t <= timeRange:
		stateVectorHighPrecision = RK4_step(RK4_step(stateVector,t,h/2),t,h/2) # test steps
		stateVectorLowPrecision = RK4_step(stateVector,t,h)

		diff = np.linalg.norm(stateVectorHighPrecision-stateVectorLowPrecision) # euclidean distance
		print("Disagreement:",diff)

		h = h * ( abs(tolerance/diff) )**0.2 # formula for best h
		print('calculated best h:',h)

		stateVector = RK4_step(stateVector,t,h)

		thetas.append(stateVector[0])
		omegas.append(stateVector[1])

		t+= h

	plt.plot(thetas,omegas,markersize=1,marker='o',linestyle='-')

plt.show()