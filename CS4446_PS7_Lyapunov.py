import numpy as np 
from matplotlib import pyplot as plt
import math
from math import pi as PI
import matplotlib.ticker as tck

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
tolerance = 0.08#
h = 0.001

# initial state
stateVector = np.array([13,-12,52])

# physical parameters
# a = 0.398
# b = 2
# c = 4
a = 16
r = 45
b = 4

def F(stateVector,t):
	x = stateVector[0]
	y = stateVector[1]
	z = stateVector[2]
	
	#return np.array([-(y + z),x+a*y,b+z*(x - c)])
	return np.array([a*(y-x),r*x-y-x*z,x*y-b*z])
	

def RK4_step(stateVector,t,h):
	k1 = F(stateVector,t)
	k2 = F(stateVector+(h/2)*k1,t+(h/2))
	k3 = F(stateVector+(h/2)*k2,t+(h/2))
	k4 = F(stateVector+h*k3,t+h)

	return stateVector+(h/6)*(k1+2*k2+2*k3+k4)

adaptiveTimeRange = 100
fixedTime = np.arange(0.0, adaptiveTimeRange, h)
x = []
y = []
z = []

x.append(stateVector[0])
y.append(stateVector[1])
z.append(stateVector[2])

# fixed time step solution
for t in fixedTime:
	stateVector = RK4_step(stateVector,t,h)

	x.append(stateVector[0])
	y.append(stateVector[1])
	z.append(stateVector[2])

# axs.plot3D(x,y,z,'gray',markersize=0.1,color='orange')

t = 0
h = 0.001
stateVector = np.array([13,-12,52])
x = []
y = []
z = []

x.append(stateVector[0])
y.append(stateVector[1])
z.append(stateVector[2])

# adaptive time steps
while t <= adaptiveTimeRange:

	stateVectorHighPrecision = RK4_step(RK4_step(stateVector,t,h/2),t,h/2) # test steps
	stateVectorLowPrecision = RK4_step(stateVector,t,h)

	diff = np.linalg.norm(stateVectorHighPrecision-stateVectorLowPrecision) # euclidean distance

	h = h * ( abs(tolerance/diff) )**0.2 # formula for best h

	stateVector = RK4_step(stateVector,t,h)

	x.append(stateVector[0])
	y.append(stateVector[1])
	z.append(stateVector[2])

	t+= h

# axs.plot3D(x,y,z,markersize=0.01,color='blue')
axs.scatter3D(x,y,z,s=1,color='blue')


plt.show()