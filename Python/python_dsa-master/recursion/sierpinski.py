#!/usr/bin/python3
"""
Draw a Sierpinski triangle
"""
import turtle


def draw(points, color, t):
    # Draw a triangle
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def mid(p1, p2):
    # Get the point halfway between two points
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, t):
    # Draw a Sierpinski triangle
    colors = ['blue', 'red', 'green', 'yellow', 'violet', 'orange']
    draw(points, colors[degree], t)
    if degree > 0:
        sierpinski([points[0], mid(points[0], points[1]),
                    mid(points[0], points[2])], degree - 1, t)
        sierpinski([points[1], mid(points[0], points[1]),
                    mid(points[1], points[2])], degree - 1, t)
        sierpinski([points[2], mid(points[2], points[1]),
                    mid(points[0], points[2])], degree - 1, t)

if __name__ == '__main__':
    t = turtle.Turtle()
    my_window = turtle.Screen()
    my_points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(my_points, 3, t)
    my_window.exitonclick()
