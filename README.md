# maze-creator

this script creates random maze.
it is inspired from a video find on YouTube, but only for the way of think to create the maze.

There is a file "maze_solver.py" but it doesn't work for now, I'm thinking about a method to solve it.

## demo 

<p  align="center">
    <img src="readme_files/demo.gif" alt="let's see readme_files/demo.gif">
</p>

as shown above, we can create a totally random maze in 3 different ways:
- by showing all steps of the creation of the maze, it only serves to show the logic
- by showing a maze directly into a window 
- by creating it into a matrix format, so it could be useful to use it if we want to solve it with algorithms.

matrix format shown in the demo.gif :
````text
[[ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1]
 [27 27 27 27 27 27  1 27 27 27 27 27  1 27  1 27 27 27  1 27  1]
 [ 1  1  1  1  1 27  1 27  1 27  1 27  1 27  1  1  1 27  1 27  1]
 [ 1 27 27 27  1 27 27 27  1 27  1 27 27 27  1 27  1 27  1 27  1]
 [ 1  1 27  1  1 27  1 27  1  1  1  1 27  1  1 27  1 27  1 27  1]
 [ 1 27 27 27 27 27  1 27  1 27 27 27 27 27 27 27 27 27 27 27  1]
 [ 1  1  1  1  1 27  1  1  1  1  1  1 27  1  1 27  1  1  1 27  1]
 [ 1 27 27 27 27 27  1 27  1 27 27 27 27 27  1 27  1 27 27 27  1]
 [ 1  1  1 27  1  1  1 27  1  1  1 27  1  1  1 27  1  1  1  1  1]
 [ 1 27  1 27 27 27 27 27  1 27  1 27 27 27  1 27  1 27 27 27  1]
 [ 1 27  1 27  1 27  1  1  1 27  1  1  1 27  1 27  1  1  1 27  1]
 [ 1 27 27 27  1 27 27 27 27 27 27 27  1 27  1 27  1 27 27 27  1]
 [ 1 27  1 27  1 27  1  1  1  1  1  1  1  1  1 27  1 27  1  1  1]
 [ 1 27  1 27  1 27 27 27 27 27  1 27  1 27 27 27  1 27  1 27  1]
 [ 1  1  1 27  1  1  1  1  1 27  1 27  1  1  1 27  1 27  1 27  1]
 [ 1 27  1 27 27 27  1 27  1 27 27 27  1 27 27 27  1 27 27 27  1]
 [ 1 27  1 27  1  1  1 27  1  1  1 27  1  1  1  1  1 27  1 27  1]
 [ 1 27  1 27 27 27  1 27 27 27  1 27 27 27  1 27 27 27  1 27  1]
 [ 1 27  1  1  1 27  1 27  1  1  1 27  1  1  1  1  1  1  1 27  1]
 [ 1 27 27 27 27 27  1 27 27 27 27 27 27 27 27 27 27 27 27 27 27]
 [ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1]]
````
all 1 are walls, and other numbers are ways.
## Before use the script
make sure you respect all dependencies.
type this command in your terminal to install all dependencies :
```bash
pip install -r requirements.txt
```
it will install the same version of matplotlib and numpy I used to code it.

## How to use the script

there is 3 main functions into the maze generator :
- create_maze() which give you a matrix representing a random maze 
- show_maze() which show you directly the maze in a window  
- show_animation_maze() which show you an animation with all steps for the creation of the maze

### here an example to know how to use them :

```python3
import maze_generator as mg

width, height = 11, 11

# we give to the maze generator the dimensions wanted
mg.init(width, height)

# we get directly the maze by this function, we can print it into matplotlib or into a prompt as we can see below 
maze = mg.create_maze()
print(maze)

# this function shows directly a random maze 
mg.show_maze()

# this function shows an animation with all steps to create a maze 
mg.show_animation_maze()
```

## Sources

- https://www.youtube.com/embed/K7vaT8bZRuk
