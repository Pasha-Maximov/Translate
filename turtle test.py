import turtle
screen = turtle.Screen()
screen.bgcolor("black")
paper = turtle.Turtle()
paper.color("blue")

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











paper.right(10)
paper.forward(20)

paper.goto(-50,-50)

paper.right(180)

for i in range(20):
    paper.forward(10)
    paper.right(9)

paper.goto(200,200)

paper.right(10)
paper.forward(20)

paper.penup()
paper.goto(-150,-150)
paper.pendown()

paper.right(180)

for i in range(20):
    paper.forward(10)
    paper.right(9)

paper.penup()
paper.goto(150,150)
paper.pendown()

paper.dot(15)

paper.penup()
paper.goto(-100,100)
paper.pendown()

paper.clear()

paper.home()

paper.clear()

paper.circle(100)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,180)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,90)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,360)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,360,6)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,360,steps=6)

paper.clear()

paper.home()

paper.clear()

paper.circle(100,180,6)

paper.clear()

paper.home()

paper.clear()

paper.right(90)

paper.circle(100,360)

paper.left(90)

paper.clear()

paper.home()

paper.clear()

paper.right(90)

paper.circle(100,360,6)

paper.left(90)

paper.clear()

paper.home()

paper.clear()

# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(0, 0, 150, 100, 0, 360)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent


# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(0, 100, 150, 100, 0, 270)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent

# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(0, 0, 150, 100, 45, 270)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent

# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(0, 50, 150, 100, 0, 180)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent

# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(50, 50, 150, 100, 90, 180)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent

# Draw a wide ellipse at a specified position, angle, and extent
draw_ellipse(50, 50, 150, 100, 90, 180)  # You can change (0, 0) to any (x, y) coordinates, set the angle, and extent

paper.clear()

paper.home()

paper.clear()

draw_ellipse(0, 0, 150, 50, 0, 360)

paper.clear()

paper.home()

paper.clear()

draw_ellipse(0, 0, 150, 25, 0, 360)

paper.clear()

paper.home()

paper.clear()

draw_ellipse(0, 0, 150, 12.5, 0, 360)

paper.clear()

paper.home()

paper.clear()

paper.goto(250,250)

paper.clear()

paper.home()

paper.clear()


# Hide the turtle
paper.hideturtle()

# Keep the window open
turtle.done()
