import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
import random as rd


def generateGrille():
    global width, height
    maze = []
    temp = []
    nbrColor = 9
    for line in range(height-1):
        paireColumn = 0
        if(line % 2):
            temp.append(1)
            for column in range(1, width-1):
                temp.append(nbrColor if column % 2 else 1)
                nbrColor += 1
            temp.append(1)
            maze.append(temp)
            temp = []
        else:
            maze.append([1 for i in range(width)])
    maze.append([1 for i in range(width)])
    maze = np.array(maze)
    if(not(width % 2 == 0 and height%2 == 0)):
        maze[height-2][width-1] = maze[height-2][width-2]
        maze[1][0] = maze[1][1]
        print("test")
    else:
        maze[1][0] = maze[1][1]
        maze[height-3][width-1] = maze[height-3][width-3]
        maze[height-3][width-2] = maze[height-3][width-3]
    return maze


def chooseRdWall():
    global maze, width, height
    wall = 0
    line, column = 0, 0
    while wall != 1:
        line, column = rd.randint(0, height-1), rd.randint(0, width-1)
        # we don't want to take the main walls
        if(line != 0 and line != 0 and column != height-1 and column != 0
                and line+1 < height and column+1 < width):
            if(maze[line+1][column] != maze[line-1][column]):
                wall = maze[line][column]
            elif(maze[line][column+1] != maze[line][column-1]):
                wall = maze[line][column]

    return line, column


def changeColor(nbrToChange, nbr):
    global maze, width, height
    if(nbr != 1 and nbrToChange != 1):
        maze[maze == nbrToChange] = nbr
    return maze


def breakWall():
    global maze, width, height
    line, column = chooseRdWall()
    if(column+1 < width and line+1 < height and column != 0 and line != 0):
        if(maze[line][column-1] != maze[line][column+1]):
            maze[line][column] = maze[line][column-1]
            changeColor(maze[line][column+1], maze[line][column-1])
        elif(maze[line-1][column] != maze[line+1][column]):
            maze[line][column] = maze[line-1][column]
            changeColor(maze[line+1][column], maze[line-1][column])
    return maze


def sameNumbersInTab(tab):
    if(tab != []):
        number = tab[0]
        for i in tab:
            if number != i:
                return 1
    return 0


def createMaze(anim=0):
    global width, height, maze, sameNumbers

    # this table have to be 100% True
    while False in sameNumbers:
        for i in range(height):
            temp = list(filter(lambda a: a != 1, maze[i].copy()))
            if(temp != []):
                temp = list(filter(lambda a: a != temp[0], temp))
                if(temp != []):
                    maze = breakWall()
                else:
                    sameNumbers[i] = True
            else:
                sameNumbers[i] = True
        if(anim):
            return maze
    print(maze)
    return maze


def showAnimationMaze():
    def update(i):
        global maze
        maze = createMaze(1)
        matrice.set_array(maze)

    fig, ax = plt.subplots()
    matrice = ax.matshow(maze)
    matrice.set_cmap(cmap=plt.cm.gnuplot2)
    ani = FuncAnimation(fig, update, frames=19, interval=1000)
    plt.show()


def showMaze():
    maze = createMaze()

    plt.pcolor(maze, cmap=plt.cm.gnuplot2)
    plt.show()


if __name__ == "__main__":

    width, height = 11, 11
    sameNumbers = [False for i in range(height)]
    maze = np.array(generateGrille())

    showAnimationMaze()
