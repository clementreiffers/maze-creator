import random as rd

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def generate_grille():
    global width, height
    maze = []
    temp = []
    nbrColor = 9
    for line in range(height - 1):
        if line % 2:
            temp.append(1)
            for column in range(1, width - 1):
                temp.append(nbrColor if column % 2 else 1)
                nbrColor += 1
            temp.append(1)
            maze.append(temp)
            temp = []
        else:
            maze.append([1 for _ in range(width)])
    maze.append([1 for _ in range(width)])
    maze = np.array(maze)
    if width % 2 != 0 or height % 2 != 0:
        maze[height - 2][width - 1] = maze[height - 2][width - 2]
        maze[1][0] = maze[1][1]
    else:
        maze[1][0] = maze[1][1]
        maze[height - 3][width - 1] = maze[height - 3][width - 3]
        maze[height - 3][width - 2] = maze[height - 3][width - 3]
    return maze


def choose_random_wall():
    global maze, width, height
    wall = 0
    line, column = 0, 0
    while wall != 1:
        line, column = rd.randint(0, height - 1), rd.randint(0, width - 1)
        # we don't want to take the main walls
        if (
            line != 0
            and column != height - 1
            and column != 0
            and line + 1 < height
            and column + 1 < width
        ):
            if (
                maze[line + 1][column] != maze[line - 1][column]
                and maze[line + 1][column] != 1
                and maze[line - 1][column] != 1
                and maze[line][column] == 1
            ):
                wall = maze[line][column]

            elif (
                maze[line][column + 1] != maze[line][column - 1]
                and maze[line][column + 1] != 1
                and maze[line][column - 1] != 1
                and maze[line][column] == 1
            ):
                wall = maze[line][column]

            else:
                ...
    return line, column


def change_color(nbrToChange, nbr):
    global maze, width, height
    if nbr != 1 and nbrToChange != 1:
        maze[maze == nbrToChange] = nbr
    return maze


def break_wall():
    global maze, width, height
    line, column = choose_random_wall()
    if (
        column + 1 < width
        and line + 1 < height
        and column != 0
        and line != 0
        and (
            (
                maze[line][column + 1] != 1
                or maze[line + 1][column] != 1
                or maze[line - 1][column] != 1
                or maze[line][column - 1] != 1
            )
        )
    ):
        if maze[line][column - 1] != maze[line][column + 1]:
            maze[line][column] = maze[line][column - 1]
            change_color(maze[line][column + 1], maze[line][column - 1])
        if maze[line - 1][column] != maze[line + 1][column]:
            maze[line][column] = maze[line - 1][column]
            change_color(maze[line + 1][column], maze[line - 1][column])
    return maze


def same_numbers_in_tab(tab):
    if tab:
        number = tab[0]
        for i in tab:
            if number != i:
                return 1
    return 0


def create_maze(anim=0):
    global width, height, maze, sameNumbers

    # this table have to be 100% True
    while False in sameNumbers:
        for i in range(height):
            if temp := list(filter(lambda a: a != 1, maze[i].copy())):
                if temp := list(filter(lambda a: a != temp[0], temp)):
                    maze = break_wall()
                else:
                    sameNumbers[i] = True
            else:
                sameNumbers[i] = True
        if anim:
            return maze
    return maze


def show_animation_maze():
    def update(i):
        global maze
        maze = create_maze(1)
        matrice.set_array(maze)

    fig, ax = plt.subplots()
    matrice = ax.matshow(maze)
    matrice.set_cmap(cmap=plt.cm.gnuplot2)
    ani = FuncAnimation(fig, update, frames=19, interval=1000)
    plt.show()


def show_maze():
    maze = create_maze()

    plt.pcolor(maze, cmap=plt.cm.gnuplot2)
    plt.show()


def init(w, h):
    global width, height, maze, sameNumbers
    width, height = w, h
    sameNumbers = [False for _ in range(height)]
    maze = np.array(generate_grille())


width, height, maze, sameNumbers = 0, 0, [], []

if __name__ == "__main__":
    width, height = 21, 21
    init(width, height)

    # if we want to show an animation
    show_animation_maze()

    # if we want to show directly a random maze
    show_maze()

    # if we want to get only a matrix representing the maze
    maze = create_maze()
    print(maze)
