import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing a Hand with Turtle")
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(5)

def draw_palm():
    pen.penup()
    pen.goto(-50, -50)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(150)
        pen.left(90)
    pen.end_fill()

def draw_finger(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

def draw_hand():
    draw_palm()
    
    finger_positions = [(-30, 100), (0, 100), (30, 100), (60, 100)]
    for pos in finger_positions:
        draw_finger(pos[0], pos[1])
    
    pen.penup()
    pen.goto(-70, 30)
    pen.pendown()
    pen.setheading(30)
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.forward(30)
    pen.right(90)
    pen.forward(15)
    pen.right(90)
    pen.forward(30)
    pen.right(90)
    pen.forward(15)
    pen.end_fill()

def main():
    draw_hand()
    pen.hideturtle()
    screen.mainloop()

main()
