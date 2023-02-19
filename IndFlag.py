from turtle import *
import turtle

# pen = turtle.Turtle()
# print(pen.position())
# pen.pensize(5)
# pen.color("navy")
# pen.circle(60)

turtle.hideturtle()
# Mini Blue Circles
penup()
goto(0, 0)
pendown()
color("navy")
for i in range(24):
    # turtle.tracer(2)
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(15)
    left(15)
    pendown()

penup()
goto(0, 0)
pendown()
pen = turtle.Turtle()
print(pen.position())


for i in range(24):
    pen.color("navy")
    pen.width(4)
    pen.forward(15)
    pen.left(15)


#Go to Center
# move back


print(pen.position())
# Spokes
pen.up()
pen.goto(8, 57)
pen.down()
pen.width(2)
for i in range(24):
    pen.forward(50)
    pen.backward(50)
    pen.left(15)

print(pen.position())
pen.up()
pen.goto(-400, 330)
# Orange Rectangle
pen.color("orange")
pen.begin_fill()
pen.forward(800)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(800)
pen.end_fill()

pen.up()

pen.left(90)
pen.forward(150)
print(pen.position())
# pen.down()
pen.color("green")
pen.left(90)
pen.begin_fill()
pen.forward(800)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(800)
pen.right(90)
pen.forward(200)
pen.end_fill()
turtle.hideturtle()




turtle.exitonclick()





# # Big Blue Circle
# penup()
# goto(0, 0)
# pendown()
# color("navy")
# begin_fill()
# circle(70)
# end_fill()
#
# # Big White Circle
# penup()
# goto(0, 0)
# pendown()
# color("white")
# begin_fill()
# circle(60)
# end_fill()