# importing turtle for graphics
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("Black")

# object
pen = turtle.Turtle()

#speed of pen


# object color
pen.pencolor("White")

# object width
pen.width(10)
tut = turtle.Screen()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.hideturtle()

turtle.speed(10)
# Code for symbol
# backward C
pen.hideturtle()
print(pen.pos())
for x in range(15):
    pen.backward(1.3)
    pen.left(1.3)

for x in range(160):
    turtle.tracer(2)
    pen.forward(1.3)
    pen.right(1.3)

# for x in range(185):
#     pen.backward(1.3)
#     pen.left(1.3)

# for x in range(185):
#     pen.forward(1.3)
#     pen.right(1.3)

for x in range(25):
    turtle.tracer(1)
    pen.backward(1.3)
    pen.left(1)
print(pen.pos())

for x in range(235):
    pen.backward(1.2)
    pen.right(1)

for x in range(80):
    turtle.tracer(2)
    pen.backward(1.2)
    pen.left(1)

pen.up()
pen.goto(24.93,-111.65)
pen.down()
pen.width(8)
pen.right(45)
pen.forward(55)
print(pen.pos())

for x in range(30):
    turtle.tracer(1)
    pen.forward(1.3)
    pen.left(1.3)

for x in range(195):
    pen.forward(1.2)
    pen.right(1.1)

pen.up()
pen.goto(45,75)
pen.down()

pen.setheading(-60)
pen.width(12)
pen.circle(80, 120)

pen.up()
pen.goto(120,65)
pen.down()
pen.circle(5)  # draw eyes
pen.end_fill()
turtle.exitonclick()
# pen.backward(10)
# for x in range(280):
#     pen.backward(2.2)
#     pen.right(1)

