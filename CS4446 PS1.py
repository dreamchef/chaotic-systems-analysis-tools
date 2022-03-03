# import matplotlib
# matplotlib.use('TkAgg')

# from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# mngr = plt.get_current_fig_manager()
# mngr.window.SetPosition(0,0,1000, 1000)

def logisticMap(x0, R, m, name):

    iterates = [x0]
    x = x0

    # Data for plotting
    for i in range(m):
        x = R * x * (1 - x)
        iterates.append(x)

    print(iterates)
    print(range(m+1))

    fig = plt.figure(name)
    axs = fig.subplots(3)
    fig.set_size_inches(15,9)
    plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)

    axs[0].plot(range(m+1), iterates, 'o', markersize=3)
    axs[0].set(xlabel='n', ylabel='x_n',title='Time-Domain')
    axs[0].grid()

    axs[1].plot(iterates[0:-2], iterates[1:-1], 'o', markersize=2)
    axs[1].set(xlabel='x_{n+1}', ylabel='x_n', title='Difference Function')
    axs[1].grid()
 
    axs[2].plot(iterates[0:-3], iterates[2:-1], 'o', markersize=2)
    axs[2].set(xlabel='x_{n+2}', ylabel='x_n', title='Two-Cycle')
    axs[2].grid()
    
    # x0Slider = Slider(axs, x0, 0, 2, valinit=x0)
    # RSlider = Slider(axs, R, 0, 10, valinit=R)
    # mSlider = Slider(axs, m, 0, 1000, valinit=m)

    plt.show()

x0 = 0.2
R = 3.95
m = 100

logisticMap(x0,R,m,"1")