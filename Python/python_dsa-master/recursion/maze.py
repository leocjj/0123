#!/usr/bin/python3
"""
Escape a maze
"""
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    # Define a Maze
    def __init__(self, maze_filename):
        # Initialize a Maze
        rows = 0
        columns = 0
        self.maze_list = []
        maze_file = open(maze_filename, 'r')
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == 'S':
                    self.start_row = rows
                    self.start_col = col
                col += 1
            rows += 1
            self.maze_list.append(row_list)
            columns = len(row_list)

        self.rows = rows
        self.columns = columns
        self.x_translate = -columns / 2
        self.y_translate = rows / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columns - 1) / 2 - .5,
                                    -(rows - 1) / 2 - .5,
                                    (columns - 1) / 2 + .5,
                                    (rows - 1) / 2 + .5)

    def draw_maze(self):
        # Draw the maze
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rows):
            for x in range(self.columns):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def draw_centered_box(self, x, y, color):
        # Draw the centered box
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        # Move the turtle
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate,
                                         -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        # Drop a breadcrumb to show where the turtle has already explored
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        # Update position
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None
        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        # Check if turtle has reached an exit
        return (row == 0 or row == self.rows - 1 or
                col == 0 or col == self.columns - 1)

    def __getitem__(self, index):
        # Get item at specified index
        return self.maze_list[index]


def search_from(maze, row, column):
    # Try each of four directions until we find a way out
    maze.update_position(row, column)
    # Base case 1: We ran into an obstacle
    if maze[row][column] == OBSTACLE:
        return False
    # Base case 2: We found a square we already explored
    if maze[row][column] == TRIED or maze[row][column] == DEAD_END:
        return False
    # Base case 3: We found an outside edge not occupied, success!
    if maze.is_exit(row, column):
        maze.update_position(row, column, PART_OF_PATH)
        return True
    maze.update_position(row, column, TRIED)

    # Try other directions as needed
    found = (search_from(maze, row - 1, column) or
             search_from(maze, row + 1, column) or
             search_from(maze, row, column - 1) or
             search_from(maze, row, column + 1))
    if found:
        maze.update_position(row, column, PART_OF_PATH)
    else:
        maze.update_position(row, column, DEAD_END)
    return found

if __name__ == '__main__':
    my_maze = Maze('maze2.txt')
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)
    search_from(my_maze, my_maze.start_row, my_maze.start_col)
