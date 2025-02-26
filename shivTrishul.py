import time
import turtle
import threading
from concurrent.futures import ThreadPoolExecutor

screen = turtle.Screen()
screen.bgcolor('black')
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

# screen.tracer(False)  # Disable auto updates

def animated_text():
    turtle.Screen().bgcolor('black')

    t = turtle.Turtle()

    t.hideturtle()
    t.color("gold")  # Set text color
    t.penup()

    # Starting position
    x, y = -150, 200

    # Animate text movement
    for _ in range(25):  # Number of steps to move
        t.clear()  # Clear previous text
        t.goto(x, y)  # Move to new position
        t.write("हर हर महादेव 🚩🙏", align="center", font=("Arial", 24, "bold"))
        x += 10  # Move text to the right
        # screen.update()  # Refresh screen
        time.sleep(0.03)# Delay for smooth animation

    for _ in range(25):  # Number of steps to move
        t.clear()  # Clear previous text
        t.goto(x, y)  # Move to new position
        t.write("हर हर महादेव 🚩🙏", align="center", font=("Arial", 24, "bold"))
        x -= 10  # Move text to the right
        # screen.update()  # Refresh screen
        time.sleep(0.03)# Delay for smooth animation

    for _ in range(20):  # Number of steps to move
        t.clear()  # Clear previous text
        t.goto(x, y)  # Move to new position
        t.write("हर हर महादेव 🚩🙏", align="center", font=("Arial", 24, "bold"))
        x += 10  # Move text to the right
        # screen.update()  # Refresh screen
        time.sleep(0.03)  # Delay for smooth animation


def making_trishul():

    t = turtle.Turtle()
    t.pencolor("#e8c423")
    t.fillcolor("#e8c423")
    t.penup()
    t.goto(0, -20)
    t.forward(5)
    t.pendown()
    t.begin_fill()

    t.seth(-82)
    t.forward(10)
    t.pendown()
    t.forward(10)
    turtle.reset()
    t.seth(190)
    # semi arc left
    t.circle(8, 180)

    turtle.reset()
    t.seth(-90)
    t.forward(60)

    # dumroo left side
    turtle.reset()
    t.seth(-187)
    t.forward(57)
    turtle.reset()
    t.seth(145)
    for i in range(180):  # for bottom curve
        t.left(0.85)
        t.forward(.10)

    # for i in range(50):  # for bottom curve
    #     t.left(3.57)
    #     t.forward(0.5)

    t.seth(-90)
    t.forward(40)

    turtle.reset()
    t.seth(-95)
    for i in range(188):  # for bottom curve
        t.left(0.81)
        t.forward(0.06)

    turtle.reset()
    t.seth(1)
    t.forward(60)

    turtle.reset()
    t.seth(-90)
    t.forward(200)

    t.circle(10, 175)

    turtle.reset()
    t.seth(90)
    t.forward(202)

    # dumroo right side start
    turtle.reset()
    t.seth(-4)
    t.forward(61)

    for i in range(185):  # for bottom curve
        t.left(0.72)
        t.forward(0.05)

    turtle.reset()
    t.seth(91)
    t.forward(41)

    for i in range(185):  # for bottom curve
        t.left(0.76)
        t.forward(0.07)
    turtle.reset()
    t.seth(184)
    t.forward(54)

    turtle.reset()
    t.seth(90)
    t.forward(60)

    # right semi circle
    t.seth(0)
    t.circle(8, 180)

    turtle.reset()
    t.seth(85)
    t.forward(20)

    turtle.reset()
    t.seth(-45)
    # start of right part og trishul
    # First Arc
    for i in range(80):  # for bottom curve
        t.left(1.1)
        t.forward(1.5)

    turtle.reset()
    for i in range(40):  # for bottom curve
        t.left(1.3)
        t.forward(1.2)

    turtle.reset()

    for i in range(50):  # for bottom curve
        t.left(0.6)
        t.forward(1.2)

    for i in range(35):  # for bottom curve
        t.right(2.6)
        t.forward(1.6)

    for i in range(35):  # for bottom curve
        t.left(1.6)
        t.backward(1.6)

    for i in range(15):  # for bottom curve
        t.left(1.6)
        t.backward(0.9)

    t.backward(15)

    for i in range(75):  # for bottom curve
        t.right(0.9)
        t.backward(0.8)

    for i in range(85):  # for bottom curve
        t.right(1)
        t.backward(0.9)

    t.backward(20)  # End of right part of trishul

    # start of middle part

    turtle.reset()
    t.seth(82)
    t.forward(22)
    turtle.reset()
    t.seth(40)
    t.forward(25)
    turtle.reset()
    t.seth(112.5)
    t.forward(106)
    turtle.reset()
    t.seth(-112.5)
    t.forward(106)
    turtle.reset()
    t.seth(-40)
    t.forward(25)
    turtle.reset()
    t.seth(-82)
    t.forward(22)
    print("Turtle Position after trishul part :", t.pos())
    t.penup()
    t.forward(26)
    t.pendown()
    turtle.reset()
    t.seth(-140)

    # start of Trishul left part
    for i in range(80):  # for bottom curve
        t.right(1.1)
        t.forward(1.5)

    turtle.reset()
    for i in range(40):  # for bottom curve
        t.right(1.3)
        t.forward(1.2)

    turtle.reset()

    for i in range(50):  # for bottom curve
        t.right(0.6)
        t.forward(1.2)

    for i in range(35):  # for bottom curve
        t.left(2.6)
        t.forward(1.6)

    for i in range(35):  # for bottom curve
        t.right(1.6)
        t.backward(1.6)

    for i in range(15):  # for bottom curve
        t.right(1.6)
        t.backward(0.9)

    t.backward(15)

    for i in range(80):  # for bottom curve
        t.left(0.9)
        t.backward(0.8)

    for i in range(76):  # for bottom curve
        t.left(1.20)
        t.forward(-1.21)

    turtle.reset()
    t.seth(95)
    t.forward(7)

    t.end_fill()
    t.hideturtle()  # Hide turtle cursor


# Start both tasks

making_trishul()
animated_text()  # Draw Trishul

turtle.exitonclick()
# Animate text

# screen.mainloop()  # Keeps the Turtle window open
