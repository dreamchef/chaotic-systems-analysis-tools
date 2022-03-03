import matplotlib.pyplot as plt
import numpy as np
import math

def drawTree(iterations, leftRatio, leftAngle, rightRatio, rightAngle):

    # ========= Plot configuration ============
    fig = plt.figure()
    axs = fig.subplots(1)
    fig.set_size_inches(15,9)
    # plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.6)
    axs.set(title='Fractal')
    axs.grid()
    plt.gca().set_aspect('equal', adjustable='box')

    # ========= Plotting ===========
    # Nested list / tree approach

    endpoints = [ [ [0,0] ] ] # tree
    for level in range(0,iterations):
        numNewBranches = 2**(level)
        endpoints.append([])
        print(numNewBranches)
        
        # add 2^(level-1) new endpoints to data structure
        for newBranchIdx in range(numNewBranches):
            lastBranchIdx = math.floor(newBranchIdx/2);
            if((level-1) % 2 == 0): # draw horizontally on even levels
                y = endpoints[level][lastBranchIdx][1]
                if(newBranchIdx % 4 == 0 or newBranchIdx % 4 == 1):
                    if(newBranchIdx % 2 == 0): # alternate left and right
                        xcomp = math.cos(math.radians(rightAngle))*rightRatio**level
                        ycomp = math.sin(math.radians(rightAngle))*rightRatio**level
                        x = endpoints[level][lastBranchIdx][0] + xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    else:
                        xcomp = math.cos(math.radians(leftAngle))*leftRatio**level
                        ycomp = math.sin(math.radians(leftAngle))*leftRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    endpoints[level+1].append([x,y])
                else:
                    if(newBranchIdx % 2 == 0): # alternate left and right
                        xcomp = math.cos(math.radians(leftAngle))*leftRatio**level
                        ycomp = math.sin(math.radians(leftAngle))*leftRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    else:
                        xcomp = math.cos(math.radians(rightAngle))*rightRatio**level
                        ycomp = math.sin(math.radians(rightAngle))*rightRatio**level
                        x = endpoints[level][lastBranchIdx][0] + xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    endpoints[level+1].append([x,y])

            else:               # draw vertically on even levels
                x = endpoints[level][lastBranchIdx][0]
                if(newBranchIdx % 4 == 0 or newBranchIdx % 4 == 1):
                    if(newBranchIdx % 2 == 0): # alternate up and down
                        xcomp = math.sin(math.radians(rightAngle))*rightRatio**level
                        ycomp = math.cos(math.radians(rightAngle))*rightRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] - ycomp
                    else:
                        xcomp = math.sin(math.radians(leftAngle))*leftRatio**level
                        ycomp = math.cos(math.radians(leftAngle))*leftRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    endpoints[level+1].append([x,y])
                else:
                    if(newBranchIdx % 2 == 0): # alternate up and down
                        xcomp = math.sin(math.radians(leftAngle))*leftRatio**level
                        ycomp = math.cos(math.radians(leftAngle))*leftRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] + ycomp
                    else:
                        xcomp = math.sin(math.radians(rightAngle))*rightRatio**level
                        ycomp = math.cos(math.radians(rightAngle))*rightRatio**level
                        x = endpoints[level][lastBranchIdx][0] - xcomp
                        y = endpoints[level][lastBranchIdx][1] - ycomp
                    endpoints[level+1].append([x,y])

            axs.plot(   # from
                [endpoints[level][lastBranchIdx][0], 
                endpoints[level+1][-1][0]],
                
                        # to
                
                [endpoints[level][lastBranchIdx][1],
                endpoints[level+1][-1][1]])

    print(endpoints)
    plt.show()

iterations = 8
leftRatio = 0.65
rightRatio = 0.7
leftAngle = 5
rightAngle = 15

drawTree(iterations, leftRatio, leftAngle, rightRatio, rightAngle)