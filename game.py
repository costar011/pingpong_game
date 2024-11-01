import turtle as t
import random
import time

def right():
    if player.xcor() < 200:
    player.forward(x+10, y)

def left():
    if player.xcor() > -200:
    player.backward(x+10, y)


t.bgcolor('skyblue')
t.setup(500, 700)

# 플레이어 설정
player = t.Turtle()
player.shape('square')
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0, -270)


t.listen()
t.onkeypress(right, 'Right')
t.onkeypress(left, 'Left')


# ball

ball - t.Turtle()