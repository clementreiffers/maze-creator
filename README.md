# MazeCreator

this script creates random maze.
it is inspired from a video find on youtube, but only for the way of think to create the maze.

## Before use the script

make this command in yout prompt to install this libraries :
-   matplotlib
-   numpy
-   random

```bash
python3 -m pip install matplotlib numpy random
```

## How to use the script

there is 3 main functions into the maze generator :
- createMaze() which give you a matrix representing a random maze 
- showMaze() which show you directly the maze in matplotib 
- showAnimationMaze() which show you an animation with all steps for the creation of the maze

### here an example to know how to use them :

```python
import mazeGenerator as mg 

width, height = 11, 11

# we give to the maze generator the dimensions wanted
mg.init(width, height)

# we get directly the maze by this function, we can print it into matplotlib or into a prompt as we can see below 
maze = mg.createMaze()
print(maze)

# this function shows directly a random maze 
showMaze()

# this function shows an animation with all steps to create a maze 
showAnimationMaze()
```

## Sources

<iframe width="560" height="315" src="https://www.youtube.com/embed/K7vaT8bZRuk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>