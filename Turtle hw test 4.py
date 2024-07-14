import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Realistic Hand Drawing with Turtle")
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(10)

def draw_palm():
    pen.penup()
    pen.goto(-50, -150)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(60, 180)  # Palm curve
    pen.forward(120)  # Palm height
    pen.circle(60, 180)  # Palm curve
    pen.forward(120)
    pen.end_fill()

def draw_finger(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.setheading(90)
    
    # Draw finger segments
    for _ in range(3):
        pen.forward(25)  # Finger length segment
        pen.right(90)
        pen.forward(15)  # Finger width
        pen.right(90)
        pen.forward(25)
        pen.right(90)
        pen.forward(15)
        pen.right(90)
    
    pen.end_fill()

def draw_nail(x, y):
    pen.penup()
    pen.goto(x + 5, y + 55)  # Nail position
    pen.pendown()
    pen.fillcolor("lightpink")
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(7, 180)  # Nail curve
    pen.right(90)
    pen.forward(14)
    pen.right(90)
    pen.circle(7, 180)
    pen.end_fill()

def draw_thumb():
    pen.penup()
    pen.goto(-70, -40)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.setheading(30)
    pen.forward(50)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(20)
    pen.end_fill()
    draw_nail(-70, -40)

def draw_hand():
    draw_palm()
    
    # Draw fingers
    finger_positions = [(-40, 0), (-10, 0), (20, 0), (50, 0)]
    for pos in finger_positions:
        draw_finger(pos[0], pos[1])
        draw_nail(pos[0], pos[1])

    draw_thumb()

def main():
    draw_hand()
    pen.hideturtle()
    screen.mainloop()

main()
