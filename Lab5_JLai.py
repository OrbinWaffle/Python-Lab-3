# Name: Joshua Lai
# Lab 5
# Completed 2/27/2022

import turtle
from turtle import *
import math

turtle.speed("fastest")
turtle.Screen().bgcolor("black")

def drawSquare(xPos, yPos, size, degrees):
   rads = math.radians(degrees)
   cornerX = -(size)/2 + xPos
   cornerY = -(size)/2 + yPos
   x = math.cos(rads) * (cornerX - xPos) - math.sin(rads) * (cornerY - yPos) + xPos
   y = math.sin(rads) * (cornerX - xPos) + math.cos(rads) * (cornerY - yPos) + yPos
   begin_fill()
   up()
   turtle.setpos(x, y)
   down()
   for j in range(4):
      forward(size)
      left(90)
   end_fill()

def drawSpiralSquare(xPos, yPos, size, clockwise):
   turtle.pensize(1)
   squareSize = size
   degreeIncrement = 0
   rotateAmount = 7
   turtle.setheading(0)
   iterations = 30
   for i in range (iterations, 0, -1):
      turtle.color(colors[i%2])
      turtle.fillcolor(colors[i%2])
      degrees = rotateAmount * degreeIncrement
      degreeIncrement += 1
      if( clockwise):
         degrees *= -1
      
      drawSquare(xPos, yPos, squareSize, degrees)

      if(not clockwise):
         left(rotateAmount)
      else:
         right(rotateAmount)

      squareSize = size * ((i-1) / iterations) ** 3

colors = ["white", "black"]
drawSpiralSquare(200, 200, 400, False)
colors = ["black", "white"]
drawSpiralSquare(-200, 200, 400, True)
colors = ["white", "black"]
drawSpiralSquare(-200, -200, 400, False)
colors = ["black", "white"]
drawSpiralSquare(200, -200, 400, True)

done()