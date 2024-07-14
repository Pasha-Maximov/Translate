import turtle
screen = turtle.Screen()
screen.bgcolor("black")
paper = turtle.Turtle()
paper.color("white")
paper.pensize(2)
paper.speed(8)

import math

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





paper.penup()
paper.back(15)
paper.color("green")
paper.pendown()
paper.begin_fill()
paper.forward(30)
paper.right(90)
paper.forward(300)
paper.right(90)
paper.forward(30)
paper.right(90)
paper.forward(300)
paper.right(90)
paper.end_fill()

paper.color("white")

paper.begin_fill()
draw_ellipse(50,0,100,20,180,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-50,0,100,20,0,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(0,50,100,25,90,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(0,-50,100,25,270,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(25,25,100,20,45,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(25,-25,100,20,135,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-25,-25,100,20,225,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-25,25,100,20,315,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(12.5,12.5,100,20,22.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(12.5,-12.5,100,20,112.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-12.5,-12.5,100,20,202.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-12.5,12.5,100,20,292.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(6.25,6.25,100,20,72.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(6.25,-6.25,100,20,162.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-6.25,-6.25,100,20,252.5,360)
paper.end_fill()
paper.begin_fill()
draw_ellipse(-6.25,6.25,100,20,342.5,360)
paper.end_fill()

paper.penup()
paper.home()
paper.back(50)
paper.pendown()
paper.right(90)
paper.color("white","yellow")
paper.begin_fill()
paper.circle(50)
paper.end_fill()
paper.color("white")
paper.left(90)

paper.penup()
paper.home()
paper.back(50)
paper.pendown()
paper.right(90)
paper.color("black")
paper.pensize(1)
paper.circle(50)
paper.pensize(2)
paper.color("white")
paper.left(90)









paper.hideturtle()

turtle.done()
