# Name: Joshua Lai
# Lab 5
# Completed 2/26/2022

import turtle
from turtle import *

turtle.speed("fastest")
turtle.Screen().bgcolor("black")
color = ["red", "yellow", "blue"]
begin_fill()
for i in range(180):
    pencolor(color[i%len(color)])
    forward(i)
    right(119)
done()