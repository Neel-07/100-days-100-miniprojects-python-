# Import the turtle package
import turtle

# Create screen object
sc = turtle.Screen()

# Create turtle object
pen = turtle.Turtle()

# Method to draw a square
def draw():
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

# Set screen size
sc.setup(600, 600)

# Set turtle speed
pen.speed(1)

# Loops to draw the chessboard
for i in range(8):
    pen.up()
    pen.setpos(0, 30 * i)
    pen.down()
    for j in range(8):
        if (i + j) % 2 == 0:
            col = 'black'
        else:
            col = 'white'
        pen.fillcolor(col)
        pen.begin_fill()
        draw()
        pen.end_fill()

pen.hideturtle()

	
	

