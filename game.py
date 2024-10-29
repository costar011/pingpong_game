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

Traceback (most recent call last):
  File "/Users/jyr/Coding/pingpong_game/game.py", line 1, in <module>
    import turtle as t
  File "/usr/local/Cellar/python@3.12/3.12.7_1/Frameworks/Python.framework/Versions/3.12/lib/python3.12/turtle.py", line 101, in <module>
    import tkinter as TK
  File "/usr/local/Cellar/python@3.12/3.12.7_1/Frameworks/Python.framework/Versions/3.12/lib/python3.12/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
    
ModuleNotFoundError: No module named '_tkinter'
pip install python-tk
ERROR: Could not find a version that satisfies the requirement python-tk (from versions: none)
ERROR: No matching distribution found for python-tk