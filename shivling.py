# importing turtle for graphics
from turtle import *
import turtle
from turtle import Screen, Turtle

# # Forming the window screen
# tut = turtle.Screen()
#
# # background color green
# tut.bgcolor("#ba6565")

color = (0.60160, 0, 0.99220)  # (154, 0, 254)
target = (0.86330, 0.47660, 0.31255)  # (221, 122, 80)
turtle.title("Python Guides")
tur = turtle.Screen()
turtle.tracer(2)

width, height = tur.window_width(), tur.window_height()

deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]

turt = Turtle()
turt.color(color)

turt.penup()
turt.goto(-width/2, height/2)
turt.pendown()

direct = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):

    turt.forward(width * direct)
    turt.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    turt.sety(y)

    direct *= -1

# object
pen = turtle.Turtle()

# # speed of pen
# turtle.tracer(2)

# object color
pen.pencolor("black")

# object width
pen.width(1)
tut = turtle.Screen()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.hideturtle()



#start of making Yellow circle
pen.width(2)
pen.up()
pen.goto(-32,-35)
pen.setheading(0)
pen.down()
pen.fillcolor("#E88D0E")
pen.begin_fill()
pen.circle(200)
pen.end_fill()
pen.up()
pen.goto(-45,0)

pen.fillcolor("black")
pen.begin_fill()

# forward part
pen.forward(300)
pen.right(90)
pen.forward(55)
pen.right(90)
pen.forward(24)
pen.right(90)
pen.forward(22)
pen.left(90)
pen.forward(5)
pen.right(90)
pen.forward(4)
pen.left(90)
pen.forward(500)

turtle.tracer(1)
# start of curve of first stack
print(pen.position())
for i in range(20):
    pen.right(1)
    pen.forward(1)

pen.right(15)
for i in range(10):
    pen.right(1)
    pen.forward(1)

pen.right(15)
for i in range(10):
    pen.right(1)
    pen.forward(1)

pen.right(15)
for i in range(5):
    pen.right(1)
    pen.forward(1)

pen.right(15)
for i in range(5):
    pen.right(1)
    pen.forward(1)

pen.right(20)
for i in range(5):
    pen.right(1)
    pen.forward(1)

pen.right(20)
for i in range(5):
    pen.right(1)
    pen.forward(1)

pen.right(16)
for i in range(5):
    pen.right(1)
    pen.forward(1)

pen.forward(250)
pen.end_fill()  # Completion of 1st stack fill colour


#Start of 2nd stcak filled with black
pen.fillcolor("black")
pen.begin_fill()
#start of 2nd stack
pen.goto(-210.00,-29.00)
pen.right(90)
pen.forward(25)
pen.left(90)
pen.forward(55)
#start of big curve
print(pen.position(),"start of big curve from left side")
for i in range(30):
    pen.right(1.8)
    pen.forward(1.2)

for i in range(25):
    pen.right(1.1)
    pen.forward(1)

for i in range(85):
    pen.left(0.5)
    pen.forward(1)

pen.left(15)
pen.forward(15)
pen.left(15)
pen.forward(25)
pen.left(10)
print(pen.position(),"Start of bottom line of 2nd stack after left side curve end")
pen.forward(50)
print(pen.position(), "2nd stack curve lower bottom part end start of right side curve")
for i in range(75):
    pen.left(0.9)
    pen.forward(1)

pen.left(3)
pen.forward(10)
pen.left(2)
pen.forward(10)
pen.left(5)
pen.forward(15)
pen.left(5)
pen.forward(15)

for i in range(35):  # for bottom curve
    pen.right(1.25)
    pen.forward(1.1)

pen.right(15)
pen.forward(10)
pen.right(23)
pen.forward(50)
pen.left(90)
pen.forward(25)
pen.end_fill()  #end of 2nd stcak filled with black

#start of 3rd Stack
#Start of 2nd stcak filled with black
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(-55.84,-174.21)
pen.down()
pen.right(180)
pen.forward(10)
pen.right(90)
print(pen.position(),"moving left")
pen.forward(20)

for i in range(55):  # for bottom curve
    pen.left(1.25)
    pen.forward(1.1)

for i in range(55):  # for bottom curve
    pen.right(1.25)
    pen.forward(1.1)
pen.forward(20)
print(pen.position(),"before moving down for last stack")
pen.left(90)
pen.forward(20)
print(pen.position(),"after moving down for last stack")
pen.left(90)
pen.forward(350)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(40)
# pen.up()
# pen.goto(-37.84,-178.21)
# pen.down()
# pen.right(180)
# pen.forward(47)
# pen.right(90)
# pen.forward(10)
# pen.left(90)
# pen.forward(25)
#
# for i in range(55):  # for bottom curve
#     pen.right(1.25)
#     pen.forward(1.1)
#
# for i in range(55):  # for bottom curve
#     pen.left(1.25)
#     pen.forward(1.1)
# pen.end_fill()
# #End of final bottom stack black fill  (
#Don't delete above code in ...

for i in range(55):  # for bottom curve
    pen.right(1.25)
    pen.forward(1.1)

for i in range(55):  # for bottom curve
    pen.left(1.24)
    pen.forward(1.1)
    
pen.left(3.5)
pen.forward(14)
pen.right(90)
pen.forward(12)
pen.left(90)
pen.forward(70)
pen.up()
pen.end_fill() # End of bottom stack black fill

#start of making shivling
pen.fillcolor("black")
pen.begin_fill()
pen.up()
pen.goto(48,0)
pen.down()
pen.setheading(90)
pen.forward(220)
pen.setheading(90)
pen.circle(80,180)
pen.forward(225)
pen.end_fill()

# start of making 3 lines and one dot circle
pen.hideturtle()
#1st line
pen.up()
pen.goto(-74,160)
pen.right(270)
pen.down()
pen.color("white")
pen.width(5)
pen.forward(85)

#2nd line
pen.up()
pen.goto(-74,145)
pen.setheading(90)
pen.right(90)
pen.down()
pen.color("white")
pen.width(5)
pen.forward(85)

#3rd line
pen.up()
pen.goto(-74,130)
pen.setheading(90)
pen.right(90)
pen.down()
pen.color("white")
pen.width(5)
pen.forward(85)

# small Circle in middle line
pen.up()
pen.goto(-32,140)
pen.down()
pen.color("Red")
pen.begin_fill()
pen.circle(5)
pen.end_fill()


# turtle.tracer(2)
turtle.exitonclick()
