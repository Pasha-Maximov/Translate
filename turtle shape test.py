import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Create a turtle named "hex"
hex = turtle.Turtle()
hex.color("blue")
hex.pensize(3)

# Draw a hexagon
for _ in range(6):
    hex.forward(100)
    hex.right(60)

hex.home()
hex.clear()

hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)

hex.home()
hex.clear()

hex.begin_fill()
hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)
hex.forward(100)
hex.right(90)
hex.end_fill()

# Hide the turtle
hex.hideturtle()

# Keep the window open
turtle.done()
