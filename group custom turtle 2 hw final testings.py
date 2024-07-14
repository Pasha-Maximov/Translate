import turtle
screen = turtle.Screen()
screen.bgcolor("black")
paper = turtle.Turtle()
paper.color("green")
paper.pensize(3)
paper.speed(8)

import math

# Function to draw an ellipse at a specified position, angle, and extent
def draw_ellipse(center_x, center_y, radius_x, radius_y, angle, extent=360):
    paper.penup()
    paper.goto(center_x + radius_x * math.cos(math.radians(angle)), center_y + radius_x * math.sin(math.radians(angle)))
    paper.pendown()

    for theta in range(int(extent) + 1):
        rad = math.radians(theta)
        x = radius_x * math.cos(rad)
        y = radius_y * math.sin(rad)
        x_rotated = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        y_rotated = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
        paper.goto(center_x + x_rotated, center_y + y_rotated)











paper.home()
draw_ellipse(0, 0, 100, 25, 0, 360)
paper.right(90)
paper.forward(100)
paper.right(34)
draw_ellipse(25, 25, 100, 25, 0, 360)
draw_ellipse(-50, 50, 100, 25, 35, 360)
draw_ellipse(-50, 50, 100, 25, 0, 180)
draw_ellipse(-50, 50, 100, 25, 45, 180)
paper.goto(200,200)



# Hide the turtle
paper.hideturtle()

# Keep the window open
turtle.done()
