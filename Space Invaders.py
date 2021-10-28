import turtle
import os
import math
import random

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")


#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    
border_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15
enemyspeed = 2

#choose a number of enemies
enemies_cnt = 5
#creat an empty list of enemies
enemies = []

#add enemies to the lists
for i in range(enemies_cnt):
    #create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)    
    enemy.setposition(x,y)


#create player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
       x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        #move the bullet to just above the player
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False
                
    
#keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop:
while True:
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -=40
                e.sety(y)
            enemyspeed *= -1
            
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -=40
                e.sety(y)
            enemyspeed *= -1

        #check for a collision bullet and enemy
        if isCollision(bullet,enemy):
            #reset bull
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)    
            enemy.setposition(x,y)

        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


    
