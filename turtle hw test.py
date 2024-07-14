import turtle

# Function to draw a line
def draw_line(t, start_pos, end_pos):
    t.penup()
    t.goto(start_pos)
    t.pendown()
    t.goto(end_pos)

# Function to draw a hand
def draw_hand():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Drawing a Hand")

    t = turtle.Turtle()
    t.speed(1) # Set turtle speed (1=slowest, 10=fastest)

    # Draw palm
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.circle(50)

    # Draw fingers
    finger_length = 100
    finger_angles = [50, 30, 0, -30, -50] # Angles for each finger

    for angle in finger_angles:
        t.penup()
        t.goto(0, -200)
        t.setheading(angle)
        t.forward(50)
        t.pendown()
        t.forward(finger_length)
        t.backward(finger_length)

    # Draw thumb
    t.penup()
    t.goto(0, -200)
    t.setheading(120)
    t.forward(50)
    t.pendown()
    t.forward(finger_length)
    t.backward(finger_length)

    t.hideturtle()
    screen.mainloop()

# Call the function to draw the hand
draw_hand()