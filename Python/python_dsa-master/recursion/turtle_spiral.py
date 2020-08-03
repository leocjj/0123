#!/usr/bin/python3
"""
Draw a spiral
"""
import turtle

my_turtle = turtle.Turtle()
my_window = turtle.Screen()


def draw_spiral(my_turtle, length):
    # Draw a spiral
    if length > 0:
        my_turtle.forward(length)
        my_turtle.right(90)
        draw_spiral(my_turtle, length - 5)

if __name__ == '__main__':
    draw_spiral(my_turtle, 100)
    my_window.exitonclick()
