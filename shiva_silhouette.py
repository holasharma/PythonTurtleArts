import turtle
import time
from turtle import Screen, Turtle

# background tint
# Deep maroon → warm orange (matches reference)
color = (0.35, 0.08, 0.06)  # dark maroon red (top)
target = (0.95, 0.45, 0.15)  # warm orange glow (bottom)
turtle.title("Shiva Art")
tur = turtle.Screen()
turtle.tracer(2)

width, height = tur.window_width(), tur.window_height()

deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]

turt = Turtle()
turt.color(color)
# turtle.tracer(0)
turt.penup()
turt.goto(-width / 2, height / 2)
turt.pendown()

direct = 1

for distance, y in enumerate(range(height // 2, -height // 2, -1)):
    turt.forward(width * direct)
    turt.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    turt.sety(y)

    direct *= -1

turtle.update()
# object
pen = turtle.Turtle()

# start drawing hill top
pen.fillcolor("black")
pen.begin_fill()
pen.penup()
pen.goto(-500, -250)
pen.color("black")
pen.pendown()
pen.setheading(75)
pen.right(65)
pen.forward(100)
pen.left(25)
pen.forward(50)
pen.right(15)
pen.forward(50)
pen.left(15)
pen.forward(50)
pen.right(40)
pen.forward(25)
pen.left(25)
print(pen.position())
for i in range(20):
    pen.right(1)
    pen.forward(1)

pen.left(75)
for i in range(45):
    pen.right(1)
    pen.forward(1)
pen.forward(25)
pen.left(10)
pen.forward(25)
for i in range(40):
    pen.right(1)
    pen.forward(1)

pen.forward(360)
pen.right(20)
for i in range(20):
    pen.right(1.1)
    pen.forward(1)
pen.forward(10)
pen.right(20)
pen.forward(10)
pen.left(30)
pen.forward(30)
pen.left(25)
pen.forward(50)
pen.right(20)
pen.forward(15)
for i in range(40):
    pen.right(1)
    pen.forward(1)

for i in range(40):
    pen.left(1)
    pen.forward(1)
pen.left(25)
pen.forward(15)
pen.right(35)
pen.forward(65)
pen.left(25)
pen.forward(35)
pen.right(35)
pen.forward(45)
# close shape to bottom of screen
pen.goto(width / 2 + 50, -height / 2 - 50)  # bottom-right
pen.goto(-width / 2 - 50, -height / 2 - 50)  # bottom-left
pen.goto(-500, -250)  # back to start

pen.end_fill()  # complete the hill top base

# Now Starting the Shiva outline

pen.hideturtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.width(1.5)

# 🔹 START POINT: left top of hill
start_x, start_y = -130, -84
pen.goto(start_x, start_y)
pen.pendown()

pen.begin_fill()

# Start of shiv left bottom curve
pen.setheading(130)
pen.forward(10)
for i in range(10):
    pen.right(1.1)
    pen.forward(1)

pen.right(25)
pen.forward(10)
pen.right(15)
pen.forward(15)
pen.left(110)
pen.forward(10)
pen.right(75)
for i in range(18):
    pen.right(1.8)
    pen.forward(1)
pen.left(75)
for i in range(12):
    pen.right(7)
    pen.forward(1)
for i in range(9):
    pen.right(7)
    pen.forward(1)
pen.forward(10)
pen.left(45)
for i in range(10):
    pen.right(4)
    pen.forward(1.3)
pen.left(55)
for i in range(30):
    pen.right(1.7)
    pen.forward(1.5)
pen.left(35)
pen.forward(13)
pen.left(45)
# left arm continuation
for i in range(20):
    pen.right(3)
    pen.forward(1.8)
pen.left(30)
pen.forward(20)
# left shoulder
print("left shoulder start", pen.position())
for i in range(35):
    pen.right(2)
    pen.forward(1.1)
for i in range(48):
    pen.left(1.8)
    pen.forward(1.1)
# face left part
for i in range(25):
    pen.left(0.5)
    pen.forward(1.1)
for i in range(40):
    pen.right(1.5)
    pen.forward(1.2)
pen.setheading(85)
# choti
for i in range(40):
    pen.right(1.1)
    pen.forward(1.2)
# top choti curve
for i in range(25):
    pen.right(6.5)
    pen.forward(0.9)
for i in range(22):
    pen.left(6.8)
    pen.forward(1.1)
for i in range(14):
    pen.left(6.8)
    pen.backward(1.1)
print("right face start", pen.position())
print(pen.heading())
pen.setheading(-50)
for i in range(18):
    pen.left(-0.7)
    pen.forward(1.1)
for i in range(18):
    pen.left(-0.7)
    pen.forward(1.1)
# right face curve
for i in range(15):
    pen.right(1.5)
    pen.forward(0.6)
for i in range(25):
    pen.right(0.001)
    pen.forward(0.9)
pen.forward(8)
# rigt shoulder
for i in range(20):
    pen.left(3.7)
    pen.forward(1.6)
pen.forward(8)
for i in range(19):
    pen.left(2)
    pen.forward(1.1)
# right shoulder curve towards arm
for i in range(25):
    pen.right(2)
    pen.forward(0.9)
pen.setheading(-51)
for i in range(15):
    pen.right(0.1)
    pen.forward(0.9)

# start of right arm
pen.setheading(-65)
for i in range(24):
    pen.left(0.4)
    pen.forward(0.9)
for i in range(26):
    pen.right(1)
    pen.forward(1.1)
# start of right forearm
pen.setheading(-55)
for i in range(12):
    pen.left(1.2)
    pen.forward(0.9)
for i in range(18):
    pen.right(1)
    pen.forward(1.1)
for i in range(8):
    pen.right(0.9)
    pen.forward(1)
pen.forward(2)
for i in range(6):
    pen.right(8.9)
    pen.forward(1)
# start of right fist
pen.setheading(-50)
for i in range(10):
    pen.left(1.8)
    pen.forward(0.9)
for i in range(9):
    pen.right(4)
    pen.forward(0.9)
for i in range(13):
    pen.left(5)
    pen.forward(1)
pen.forward(2)
# right fist thumb start
for i in range(13):
    pen.right(6)
    pen.forward(0.9)
pen.right(50)
pen.forward(3)
pen.left(50)
pen.forward(4)
for i in range(10):
    pen.left(0.5)
    pen.forward(1)
for i in range(7):
    pen.right(9)
    pen.forward(0.9)
pen.right(70)
pen.forward(5)
# start of right thigh end
pen.left(140)
pen.forward(13)
for i in range(10):
    pen.left(2.5)
    pen.forward(1)
for i in range(15):
    pen.right(3.5)
    pen.forward(1.1)
for i in range(17):
    pen.right(3.7)
    pen.forward(1.2)
pen.forward(2.5)
# ----------------End of Shiva Outer Body----------------
# Start of Shive Inner body

pen.setheading(180)
pen.forward(38)

print("Position when moving to top towards right arm to complete", pen.position())
# moving to top to start making right arm
pen.up()
pen.setheading(90)
pen.forward(47)
pen.down()
pen.forward(7)
pen.left(35)
for i in range(10):
    pen.left(2.5)
    pen.forward(1)
for i in range(15):
    pen.right(1.5)
    pen.forward(1)
for i in range(35):
    pen.right(0.6)
    pen.forward(1)
pen.left(24)
pen.forward(19)
# start of right underarm
pen.left(45)
for i in range(8):
    pen.left(2.5)
    pen.forward(1.2)
pen.left(48)
pen.forward(15)

for i in range(28):
    pen.left(0.7)
    pen.forward(1.2)
pen.left(90)
pen.forward(5)
pen.right(45)
for i in range(6):
    pen.right(2.5)
    pen.forward(1.2)
pen.setheading(75)
for i in range(12):
    pen.left(0.9)
    pen.forward(1.1)
pen.left(25)
for i in range(16):
    pen.right(1.1)
    pen.backward(1.1)
for i in range(5):
    pen.right(3.5)
    pen.backward(1.1)
pen.setheading(0)
for i in range(10):
    pen.right(3.5)
    pen.forward(1.2)
for i in range(33):
    pen.left(1.5)
    pen.forward(1.2)
pen.forward(11)
for i in range(30):
    pen.right(0.5)
    pen.backward(1.1)
pen.backward(170)
pen.setheading(90)
pen.forward(4)
pen.setheading(180)
pen.circle(-10, 130)  # small inward left waist curve
pen.forward(4)
# start of left waist till underarm
for i in range(8):
    pen.right(8.5)
    pen.forward(0.8)
pen.setheading(90)
pen.forward(15)
for i in range(25):
    pen.left(2)
    pen.forward(1.1)
for i in range(10):
    pen.right(2)
    pen.forward(1.1)
# start of underarm
pen.right(45)
for i in range(7):
    pen.left(2.5)
    pen.backward(1)
for i in range(10):
    pen.right(8.5)
    pen.backward(1)
pen.left(15)
for i in range(5):
    pen.right(8.5)
    pen.backward(1)
pen.setheading(220)
pen.forward(15)
for i in range(12):
    pen.left(2.3)
    pen.forward(1)
for i in range(12):
    pen.right(0.5)
    pen.forward(1)
for i in range(12):
    pen.right(1.7)
    pen.forward(1)
for i in range(12):
    pen.right(1.7)
    pen.forward(1)
for i in range(3):
    pen.right(2.7)
    pen.forward(1)
pen.left(45)
pen.forward(12)
pen.left(25)
for i in range(30):
    pen.left(4.5)
    pen.forward(0.4)
for i in range(30):
    pen.right(1.5)
    pen.forward(0.4)
pen.forward(30)
for i in range(30):  # last left body wasit curve to complete
    pen.left(0.7)
    pen.forward(1)
print("Position when completing last left wasit curve ", pen.position())

pen.up()
pen.goto(178.38, -85.17)
pen.down()
pen.setheading(180)
pen.forward(200)
pen.end_fill()
pen.up()
pen.goto(-24.48, -42.86)
pen.down()
pen.setheading(2)  # slight downward angle
for _ in range(40):
    pen.left(0.001)  # bend downward
    pen.forward(1)
pen.setheading(-0.5)
for _ in range(80):
    pen.left(0.001)  # bend downward
    pen.forward(1.1)
pen.right(1.5)
for _ in range(20):
    pen.left(0.001)  # bend downward
    pen.forward(1)
pen.right(1.5)
for _ in range(2):
    pen.left(0.001)  # bend downward
    pen.forward(1)
print("Position when completing last right wasit curve ", pen.position())
for _ in range(53):
    pen.left(0.2)  # bend downward
    pen.forward(1)
print("Position reached ", pen.position())
pen.setheading(-90)  # straight down
for _ in range(44):
    pen.forward(1)
print("Position reached ", pen.position())
pen.setheading(180)  # straight up
pen.forward(202)
print("Position reached ", pen.position())
pen.setheading(90)
pen.forward(40)
print("Position reached ", pen.position())
pen.end_fill()
pen.setheading(-10)
pen.forward(10)
pen.width(30)
pen.forward(190)
pen.up()
pen.goto(-24.48, -42.86)
pen.forward(30)
pen.setheading(-10)
pen.width(1)
pen.down()
pen.forward(10)
pen.width(50)
pen.forward(100)
pen.setheading(0)
for _ in range(85):
    pen.right(0.01)  # bend downward
    pen.forward(1.2)
pen.width(1)

# Shiva bocy complete now, Start of Trishul
pen.up()
pen.goto(-90, -84)
pen.pendown()
pen.width(5)
pen.setheading(90)
pen.forward(230)
# start of left dumroo part
pen.begin_fill()
pen.width(2)
pen.left(115)
pen.forward(18)
for _ in range(15):
    pen.right(8.5)  # bend downward
    pen.forward(1.2)
pen.setheading(90)
pen.forward(18)
for _ in range(15):
    pen.right(7.5)  # bend downward
    pen.forward(0.9)
pen.forward(18)
print("come back from where width 5 line will resume again ", pen.position())
pen.setheading(0)
pen.forward(5)
pen.left(25)
# start of right dumroo part
pen.forward(17)
for _ in range(15):
    pen.right(7.5)  # bend downward
    pen.forward(0.9)
pen.forward(19)
for _ in range(15):
    pen.right(8.5)  # bend downward
    pen.forward(0.9)
pen.left(25)
pen.forward(19)
pen.end_fill()
# Now start from top of dumroo continuing the trishul main part
pen.up()
pen.goto(-90.40, 165.13)
pen.down()
pen.setheading(90)
pen.width(5)
pen.forward(30)
print("Current Position before starting Trishul Prongs ", pen.position())
pen.begin_fill()
# start of right trishul part
pen.width(2)
pen.setheading(-45)
for i in range(8):  # for  curve
    pen.left(1.5)
    pen.forward(1.5)
for i in range(5):  # for  curve
    pen.left(1.4)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(3.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(3.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(3.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(2.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(1.9)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(3.9)
    pen.forward(1.2)
for i in range(12):  # for  curve
    pen.right(6.3)
    pen.forward(1.2)
pen.setheading(-120)
pen.forward(10)
for i in range(9):  # for  curve
    pen.left(3.9)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(1.9)
    pen.forward(1)
pen.right(35)
pen.forward(9)
for i in range(3):  # for  curve
    pen.right(4.9)
    pen.forward(0.5)
pen.right(15)
for i in range(3):  # for  curve
    pen.right(4.9)
    pen.forward(0.5)

for i in range(9):  # for  curve
    pen.right(6)
    pen.forward(1)
pen.forward(12)
for i in range(9):  # for  curve
    pen.right(5.1)
    pen.forward(1)
print("position of right prong curve end ", pen.position())
pen.setheading(90)
pen.forward(15)
pen.setheading(60)
pen.forward(9)
pen.setheading(110)
pen.forward(24)
pen.setheading(-110)
pen.forward(24)
pen.setheading(-60)
pen.forward(12)
pen.setheading(-90)
pen.forward(75)
pen.end_fill()
# end of right prong and middle part
# now start of left prong
pen.up()
pen.goto(-90.40, 195.13)
pen.down()
pen.begin_fill()
pen.width(2)
pen.setheading(-120)

for i in range(8):  # for curve
    pen.right(2.4)
    pen.forward(1)

for i in range(5):
    pen.right(1.4)
    pen.forward(1.2)

for i in range(9):
    pen.right(3.3)
    pen.forward(1.2)

for i in range(9):
    pen.right(3.3)
    pen.forward(1.2)
####
for i in range(9):  # for  curve
    pen.right(3.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.right(3.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.right(2.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.right(1.9)
    pen.forward(1.2)
####
for i in range(6):  # for  curve
    pen.right(3.9)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(6.3)
    pen.forward(1.2)
for i in range(9):  # for  curve
    pen.left(1.3)
    pen.backward(1.2)
for i in range(9):  # for  curve
    pen.right(4.3)
    pen.backward(1.2)
for i in range(9):  # for  curve
    pen.right(0.3)
    pen.backward(0.5)
pen.setheading(-85)
for i in range(9):  # for  curve
    pen.left(1.3)
    pen.forward(0.7)
for i in range(9):  # for  curve
    pen.left(1.3)
    pen.forward(0.8)
for i in range(9):  # for  curve
    pen.left(5.3)
    pen.forward(0.3)
for i in range(9):  # for  curve
    pen.left(5.3)
    pen.forward(0.3)
pen.right(15)
for i in range(9):  # for  curve
    pen.left(1)
    pen.forward(0.3)
for i in range(9):  # for  curve
    pen.left(1)
    pen.forward(0.3)
for i in range(9):  # for  curve
    pen.left(0.1)
    pen.forward(0.9)
pen.forward(7)
pen.end_fill()
# End of Shiva Body
# start of snake from neck
pen.up()
pen.goto(-7, 125)
pen.down()
pen.begin_fill()
pen.setheading(170)
pen.width(10)
for i in range(19):  # for  curve
    pen.right(1.1)
    pen.forward(1.2)
pen.width(5)
for i in range(22):  # for  curve
    pen.right(3.6)
    pen.forward(1.2)
for i in range(22):  # for  curve
    pen.left(4.5)
    pen.forward(1.2)
for i in range(15):  # for  curve
    pen.left(1.5)
    pen.backward(1.2)
for i in range(18):  # for  curve
    pen.right(6.5)
    pen.backward(1.2)
for i in range(15):  # for  curve
    pen.right(0.9)
    pen.backward(0.5)
for i in range(15):  # for  curve
    pen.right(0.2)
    pen.backward(0.1)
for i in range(15):  # for  curve
    pen.right(0.1)
    pen.backward(0.1)
for i in range(15):  # for  curve
    pen.left(0.1)
    pen.backward(0.1)
for i in range(15):  # for  curve
    pen.left(0.2)
    pen.backward(0.1)
for i in range(15):  # for  curve
    pen.left(1.2)
    pen.backward(1.1)
pen.end_fill()
# # -------- TEXT SECTION --------
# pen.up()
# pen.color("#f2d6b3")   # soft warm off-white (matches glow vibe)
#
# # Happy (smaller, cursive style feel)
# pen.goto(50, -180)
# pen.setheading(0)
# pen.write("Happy", align="center", font=("Lucida Handwriting", 20, "normal"))
#
# # Maha Shivratri (main text)
# pen.goto(50, -215)
# pen.write("Maha Shivratri", align="center", font=("Times New Roman", 32, "bold"))
#
# # OM NAMAH SHIVAY (small subtitle)
# pen.goto(55, -250)
# pen.write("OM NAMAH SHIVAY", align="center", font=("Arial", 14, "normal"))

pen.up()
pen.color("#f5e6d3")


# -------- ANIMATED TEXT --------
def animated_text():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("#f2d6b3")

    # Start from left side
    x = -300
    y1 = -180
    y2 = -215
    y3 = -250

    # Slide to right
    for _ in range(60):
        t.clear()

        t.goto(x, y1)
        t.write("Happy", align="center", font=("Lucida Handwriting", 20, "normal"))

        t.goto(x, y2)
        t.write("Maha Shivratri", align="center", font=("Times New Roman", 32, "bold"))

        t.goto(x, y3)
        t.write("OM NAMAH SHIVAY", align="center", font=("Arial", 14, "normal"))

        x += 6  # control speed here
        time.sleep(0.03)

    # Final position in center
    t.clear()

    t.goto(55, y1)
    t.write("Happy", align="center", font=("Lucida Handwriting", 20, "normal"))

    t.goto(55, y2)
    t.write("Maha Shivratri", align="center", font=("Times New Roman", 32, "bold"))

    t.goto(55, y3)
    t.write("OM NAMAH SHIVAY", align="center", font=("Arial", 14, "normal"))


animated_text()

# -------- SLIDING TEXT ANIMATION End--------

# ---------------- DONE ----------------
# turtle.update()
turtle.exitonclick()
