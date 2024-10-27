import turtle as t
import random
import time

t.bgcolor('skyblue')
t.setup(500, 700)

# 플레이어 설정
player = t.Turtle()
player.shape('square')
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0, -270)