#!/usr/bin/python3
"""
Draw a tree
"""
import turtle


def tree(length, t):
    # Draw a tree
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length - 15, t)
        t.left(40)
        tree(length - 10, t)
        t.right(20)
        t.backward(length)

if __name__ == '__main__':
    t = turtle.Turtle()
    my_window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(75, t)
    my_window.exitonclick()
