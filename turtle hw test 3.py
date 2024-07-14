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
    pen.goto(-50, -100)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(50, 180)  # Palm curve
    pen.forward(100)  # Palm height
    pen.circle(50, 180)  # Palm curve
    pen.forward(100)
    pen.end_fill()

def draw_finger(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("peachpuff")
    pen.begin_fill()
    pen.setheading(90)
    pen.forward(80)  # Finger length
    pen.right(90)
    pen.forward(20)  # Finger width
    pen.right(90)
    pen.forward(80)
    pen.right(90)
    pen.forward(20)
    pen.end_fill()

def draw_nail(x, y):
    pen.penup()
    pen.goto(x + 5, y + 70)  # Nail position
    pen.pendown()
    pen.fillcolor("lightpink")
    pen.begin_fill()
    pen.setheading(90)
    pen.circle(5, 180)  # Nail curve
    pen.right(90)
    pen.forward(10)
    pen.right(90)
    pen.circle(5, 180)
    pen.end_fill()

def draw_hand():
    draw_palm()
    
    # Draw fingers
    finger_positions = [(-40, 0), (-10, 0), (20, 0), (50, 0)]
    for pos in finger_positions:
        draw_finger(pos[0], pos[1])
        draw_nail(pos[0], pos[1])

    # Draw thumb
    pen.penup()
    pen.goto(-70, -30)
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
    draw_nail(-70, -30)

def main():
    draw_hand()
    pen.hideturtle()
    screen.mainloop()

main()
