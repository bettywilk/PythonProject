"""
This is the Template Repl for Python with Turtle.
Python with Turtle lets you make graphics easily in Python.
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)
# Begin!
t = turtle.Turtle()
# t.color('white')  sets color to white
# t.right(90)   turns right
# t.forward(75)
# draws a star in red uses a loop
for c in ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']:
    t.color(c)
    t.forward(40)
    t.left(90)
    t.color(c)
    t.forward(40)
    t.right(120)
# second gate  mine draws a triangle, does not use a loop
t.penup()  # lifts pen, no drawing
t.left(90)  # turns left
t.forward(100)
t.pendown()
t.color('green')
t.forward(75)
t.left(120)
t.forward(75)
t.left(120)
t.forward(75)

screen.mainloop()
