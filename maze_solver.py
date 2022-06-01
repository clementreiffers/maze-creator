import maze_generator as mg
import matplotlib.pyplot as plt


def resolve_maze(maze):
    width = len(maze[0]) - 1
    height = len(maze) - 1

    # first queue with the position of the end and the nbr of case since release
    queues = [[width - 1, height - 2, 0]]
    is_finish = False

    while not is_finish:
        for i in queues:
            x = i[0]
            y = i[1]
            nbr_case = i[2]
            print("x:", x, "y:", y, "nbr", nbr_case)
            if maze[x - 1, y] != 1 and x > 1:
                nbr_case += 1
                maze[x - 1, y] = nbr_case
                queues.append([x - 1, y, nbr_case])

            if maze[x + 1, y] != 1:
                nbr_case += 1
                maze[x - 1, y] = nbr_case
                queues.append([x - 1, y, nbr_case])

            if maze[x, y - 1] != 1 and y > 1:
                nbr_case += 1
                maze[x, y - 1] = nbr_case
                queues.append([x - 1, y, nbr_case])

            if maze[x, y + 1] != 1:
                nbr_case += 1
                maze[x, y + 1] = nbr_case
                queues.append([x - 1, y, nbr_case])

            queues.remove(i)
            if x == 0 and y == 1:
                is_finish = True
            print("queue:", queues)
    return maze


if __name__ == "__main__":
    width, height = 11, 11

    mg.init(width, height)

    maze = mg.create_maze()

    maze = resolve_maze(maze)

    plt.plot(maze)
    plt.show()
