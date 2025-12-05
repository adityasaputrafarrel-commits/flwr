import turtle

# Setup the turtle
t = turtle.Turtle()
t.speed(10)

# Colors for petals
petal_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]

# Function to draw a petal
def draw_petal(color):
    t.color(color)
    t.begin_fill()
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    t.end_fill()

# Draw 8 petals
for i in range(8):
    draw_petal(petal_colors[i])
    t.right(45)

# Draw the center of the flower with concentric circles
t.penup()
t.goto(0, -50)
t.pendown()
center_colors = ["yellow", "orange", "red"]
for i, color in enumerate(center_colors):
    t.color(color)
    t.begin_fill()
    t.circle(50 - i*10)
    t.end_fill()

# Draw the stem
t.penup()
t.goto(0, -100)
t.pendown()
t.color("green")
t.pensize(5)
t.setheading(270)  # Down
t.forward(150)

# Draw leaves
t.penup()
t.goto(-20, -150)
t.pendown()
t.begin_fill()
t.circle(30, 180)
t.end_fill()

t.penup()
t.goto(20, -150)
t.pendown()
t.begin_fill()
t.circle(30, 180)
t.end_fill()

# Add text "for angel"
t.penup()
t.goto(0, 120)
t.pendown()
t.color("black")
t.write("for angel", align="center", font=("Arial", 20, "bold"))

# Hide the turtle and finish
t.hideturtle()
turtle.done()
