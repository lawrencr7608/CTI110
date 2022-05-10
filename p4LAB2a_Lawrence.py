import turtle
wn = turtle.Screen()

square = turtle.Turtle() #turtle 1
square.color("lightblue")
square.pensize(10)
square.shape("turtle")

triangle = turtle.Turtle() #turtle 2
triangle.color("lightpink")
triangle.pensize(8)
triangle.shape("turtle")

for i in range(4):
    square.forward(200)
    square.right(90)

triangle.left(180)
triangle.penup()
triangle.forward(100)
triangle.pendown()

for j in range(3):
    triangle.forward(150)
    triangle.right(240)
    
    
