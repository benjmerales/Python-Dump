import turtle
import os
import math
import random

#set-up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw border
bp = turtle.Turtle()
bp.speed(0)
bp.color("white")
bp.shape('circle')
bp.penup()
bp.setposition(-300,-300)
bp.pensize(3)
bp.pendown()
for side in range(4):
    bp.fd(600)
    bp.lt(90)
bp.hideturtle()

def initPlank(x, y):
    p = turtle.Turtle()
    p.color('gray')
    p.shape('circle')
    p.penup()
    p.speed(0)
    p.setposition(x,y)
    p.pensize(5)
    p.pendown()
    p.lt(90)
    p.fd(100)
    p.lt(180)
    p.fd(50)
    #p.hideturtle()    
    return p

#create objects
p1 = initPlank(-250,-100)
p2 = initPlank(250, -100)

#create ball
b = turtle.Turtle()
b.speed(0)
b.shape('circle')
b.color('white')
b.setposition(0,0)
b.pendown()
b.lt(random.randint(-180,180))
b.penup()
def checkToBounce(object):
    print(object.getlt())
    if object.xcor() > 280:
        print("end of line A")
        object.lt(random.randint(160,180))    
    if object.xcor() < -280:
        print("end of line B")
        object.lt(random.randint(160,180))
    if object.ycor() > 280:
        print("end of line C")
        object.lt(random.randint(160,180))
    if object.ycor() < -280:
        print("end of line D")
        object.lt(random.randint(160,180))
    object.fd(5)

spd = 10
def move_up1():
    y = p1.ycor()
    y += spd
    if y > 280:
       y = -280
    p1 = initPlank(-250, y)

def move_down1():
    
    y = p1.ycor()
    y -= spd
    if y < -280:
       y = -280
    p1 = initPlank(-250, y)

def move_up2():
    y = p2.ycor()
    y += spd
    if y > 280:
       y = -280
    p1 = initPlank(-250, y)

def move_down2():
    y = p2.ycor()
    y -= spd
    if y < -280:
       y = -280
    p2 = initPlank(-250, y)
    
#keyboard bindings
turtle.listen()
turtle.onkey(move_up1, "w")
turtle.onkey(move_down1, "s")

turtle.onkey(move_up2, "Up")
turtle.onkey(move_down2, "Down")
#main game loop    
while True:
    checkToBounce(b)
    
