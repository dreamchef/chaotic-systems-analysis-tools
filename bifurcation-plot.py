# import matplotlib
# matplotlib.use('TkAgg')

# from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# mngr = plt.get_current_fig_manager()
# mngr.window.SetPosition(0,0,1000, 1000)

def logisticMapBifurcation(x0, m, l):

    iterates = [x0]
    x = x0

    valuesR = np.linspace(2.8,4,m)

    # Data for plotting
    for R in valuesR[0:-1]:
        x = R * x * (1 - x)
        iterates.append(x)

    fig = plt.figure()
    axs = fig.subplots(1)
    plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)

    axs.plot(valuesR[l+1:], iterates[l+1:], '.', markersize=1)
    axs.set(xlabel='R', ylabel='x_n',title='Bifurcation Diagram')
    axs.grid()

    plt.show()

def HenonMapBifurcation(x0,y0,m,l):

    iteratesX = [x0]
    iteratesY = [y0]
    x = x0
    prev_x = x0
    y = y0
    b = 0.3

    values_a = np.linspace(2.8,4,m)

    # Data for plotting

    for a in values_a[0:-1]:
        prev_x = x
        x = y + 1 - a * x**2
        y = b * prev_x
        iteratesX.append(x)
        iteratesY.append(y)

    print(iteratesX)
    print(iteratesY)

    axs = plt.axes(projection='3d')

    axs.scatter3D(values_a[l+1:], iteratesX[l+1:], iteratesY[l+1:], 'gray')
    axs.set(xlabel='a', ylabel='x_n', zlabel='y_n',title='Bifurcation Diagram for Henon Map')
    axs.grid()

    plt.show()


x0 = 0.1
y0 = 0.1
m = 25
l = 10

# logisticMapBifurcation(x0,m,l)

HenonMapBifurcation(x0,y0,m,l)