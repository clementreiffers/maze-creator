from venv import create
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
import random as rd


def genererGrille(width, height):
    grille = []
    temp = []
    paireColumn = 0
    paireLine = 0
    nbrColor = 9
    for line in range(height-1):
        if(paireLine % 2):
            temp.append(1)
            for column in range(1, width-1):
                temp.append(nbrColor if paireColumn % 2 else 1)
                paireColumn += 1
                nbrColor += 1
            temp.append(1)
            grille.append(temp)
            temp = []
        else:
            grille.append([1 for i in range(width)])
            paireColumn += 1
        paireLine += 1
    grille.append([1 for i in range(width)])
    grille = np.array(grille)

    grille[height-2][width-1] = grille[height-2][width-2]
    grille[1][0] = grille[1][1]
    return grille


def chooseRdWall(grille, width, height):
    wall = 0
    line, column = 0, 0
    while wall != 1:
        line, column = rd.randint(0, height-1), rd.randint(0, width-1)
        # we don't want to take the main walls
        if(line != 0 and line != 0 and column != height-1 and column != 0):
            wall = grille[line, column]

    return line, column


def changeColor(nbrToChange, nbr, grille):
    for line in range(len(grille)-1):
        for column in range(len(grille)-1):
            if(grille[line][column] == nbrToChange and nbr != 1 and nbrToChange != 1):
                grille[line][column] = nbr
                if(column == width-2 and line==height-2):
                    grille[line][column+1] = nbr
    return grille


def breakWall(grille, width, height):
    line, column = chooseRdWall(grille, width, height)
    if(column+1 < width and line+1 < height and column != 0 and line != 0):
        if(grille[line][column-1] != grille[line][column+1]):
            grille[line][column] = grille[line][column-1]
            changeColor(grille[line][column+1], grille[line][column-1], grille)
        if(grille[line-1][column] != grille[line+1][column]):
            grille[line][column] = grille[line-1][column]
            changeColor(grille[line+1][column], grille[line-1][column], grille)
    return grille


def sameNumbersInTab(tab):
    if(tab != []):
        number = tab[0]
        for i in tab:
            if number != i:
                return 1
    return 0


def createMaze(grille, width, height):
    maze = grille.copy()
    # this table have to be 100% True
    sameNumbers = [False for i in range(height)]
    while False in sameNumbers :
        for i in range(height):
            temp = list(filter(lambda a: a != 1,maze[i].copy()))
            if(temp != []):
                temp = list(filter(lambda a: a != temp[0], temp))
                if(temp != []):
                    maze = breakWall(maze, width, height)
                else:
                    sameNumbers[i] = True
            else:
                sameNumbers[i] = True
        # yield maze
        return maze

width, height = 101, 101
nbr = 0

maze = np.array(genererGrille(width, height))

M=np.array([[0,0,100,100,100,100,100,100,300,300,300,300,300,300,500,500,500,500,500,500,1000,1000,1000,1000] for i in range(0,20)]) 

def update(i):
    global maze
    maze = createMaze(maze, width, height)
    matrice.set_array(maze)

fig, ax = plt.subplots()
matrice = ax.matshow(maze)
plt.colorbar(matrice)

ani = FuncAnimation(fig, update, frames=19, interval=500)
plt.show()





# fig, ax = plt.subplots()
# matrice = ax.matshow(maze)
# plt.colorbar(matrice)

# ani = FuncAnimation(fig, createMaze(maze, width, height), frames=19, interval=500)
# plt.show()


# maze = createMaze(maze, width, height)
# plt.pcolor(maze, cmap=plt.cm.gnuplot2)
# fig = plt.figure(figsize=(5,2))
# anim = FuncAnimation(fig,frames=createMaze(maze, width, height),interval=100)
# plt.show()