import turtle as t
import random
import time

def right():
    if player.xcor() < 200:
        player.forward(10)

def left():
    if player.xcor() > -200:
        player.backward(10)

t.bgcolor('skyblue')
t.setup(500, 700)

# 플레이어 설정
player = t.Turtle()
player.shape('square')
player.shapesize(1, 5)
player.up()
player.speed(0)
player.goto(0, -270)

t.listen()
t.onkeypress(right, 'Right')
t.onkeypress(left, 'Left')

game_on = True

ball_xspeed = 5
ball_yspeed = 5

While game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1
    
    if ball.ycor() > 340:
        ball_yspeed *= -1