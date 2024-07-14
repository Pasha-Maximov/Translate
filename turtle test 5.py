import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("gray")

# Draw the hand
hand = turtle.Turtle()
hand.color("lightcoral")
hand.pensize(5)

# Function to draw a finger
def draw_finger(x, y, length):
    hand.penup()
    hand.goto(x, y)
    hand.pendown()
    hand.setheading(90)
    hand.forward(length)
    hand.right(90)
    hand.forward(30)
    hand.right(90)
    hand.forward(length)
    hand.right(90)
    hand.forward(30)
    hand.right(90)

# Draw fingers
fingers = [70, 90, 100, 90, 70]
x_positions = [-50, -20, 10, 40, 70]

for i in range(5):
    draw_finger(x_positions[i], -100, fingers[i])

# Draw the palm
hand.penup()
hand.goto(-70, -100)
hand.pendown()
hand.begin_fill()
hand.circle(70)
hand.end_fill()

# Hide the turtle
hand.hideturtle()

# Keep the window open
turtle.done()
