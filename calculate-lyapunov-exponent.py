from time import time
import numpy as np 
from matplotlib import pyplot as plt
import math
from math import pi as PI
import matplotlib.ticker as tck

# integration method
def RK4_step(stateVector,t,h):
	k1 = F(stateVector,t)
	k2 = F(stateVector+(h/2)*k1,t+(h/2))
	k3 = F(stateVector+(h/2)*k2,t+(h/2))
	k4 = F(stateVector+h*k3,t+h)

	return stateVector+(h/6)*(k1+2*k2+2*k3+k4)

# integrand
def F(stateVector,t):
	x = stateVector[0]
	y = stateVector[1]
	z = stateVector[2]


	dxx = stateVector[3]
	dxy = stateVector[4]
	dxz = stateVector[5]

	dyx = stateVector[6]
	dyy = stateVector[7]
	dyz = stateVector[8]

	dzx = stateVector[9]
	dzy = stateVector[10]
	dzz = stateVector[11]

	return np.array([
		a*(y-x), # system
		r*x-y-x*z, 
		x*y-b*z,

		-a*dxx+a*dxy, # variational equations
		-a*dyx+a*dyy,
		-a*dzx+a*dzy,

		(r-z)*dxx-dxy-x*dxz,
		(r-z)*dyx-dyy-x*dyz,
		(r-z)*dzx-dzy-x*dzz,

		y*dxx+x*dxy-b*dxz,
		y*dyx+x*dyy-b*dyz,
		y*dzx+x*dzy-b*dzz
		])

# matplotlib setup
fig = plt.figure()
fig.set_size_inches(21,10)
plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)
plt.grid(True)
axs = plt.axes(projection='3d')
# axs.set_xlim([40,-20])
# axs.set_ylim([-20,0])
# axs.set_zlim([40,80])
axs.set_xlabel('z')
axs.set_ylabel('y')
axs.set_xlabel('x')

# integration parameters
tolerance = 0.08
h = 0.001
timeRange = 0.1
t = 0

# system parameters
a = 16
r = 45
b = 4

# initial state
stateVector = np.array([0,-1,2,1,0,0,0,1,0,0,0,1])
#0,1,2,1,0,0,0,1,0,0,0,1
#10, -5, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1

trajectory = []

# fixed time step solution
while(t <= timeRange):
	stateVector = RK4_step(stateVector,t,h)
	trajectory.append(stateVector)
	t += h
print(stateVector[3:])
print(stateVector[3]+stateVector[6]+stateVector[9])
print(stateVector[4]+stateVector[7]+stateVector[10])
print(stateVector[5]+stateVector[8]+stateVector[11])