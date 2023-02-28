# Name: Joshua Lai
# Lab 5
# Completed 2/27/2022

import turtle
from turtle import *
import math

turtle.speed("fastest")
turtle.Screen().bgcolor("black")

# Draws a square centered around (xPos, yPos) of size "size" and rotated "degrees" degrees
def drawSquare(xPos, yPos, size, degrees):
   rads = math.radians(degrees)
   # Get the bottom left corner coordinate
   cornerX = -(size)/2 + xPos
   cornerY = -(size)/2 + yPos
   # Rotate the corner coordinate about the center of the square
   # First translate the sqaure to the origin, then use trigonometry to rotate it, then move it back
   x = math.cos(rads) * (cornerX - xPos) - math.sin(rads) * (cornerY - yPos) + xPos
   y = math.sin(rads) * (cornerX - xPos) + math.cos(rads) * (cornerY - yPos) + yPos
   begin_fill()
   # Move the turtle to the square corner spot, lifting up its tail so that it does not adraw a line on the way
   up()
   turtle.setpos(x, y)
   down()
   # Draw the four sides of the square
   for j in range(4):
      forward(size)
      left(90)
   end_fill()

# Draws a square with a spiraling pattern inside, centered at (xPos, yPos) of size "size".
# "Clockwise" determines if the spiral rotates clockwise or counter-clockwise
def drawSpiralSquare(xPos, yPos, size, clockwise):
   turtle.pensize(1)
   squareSize = size
   degreeIncrement = 0
   rotateAmount = 7
   turtle.setheading(0)
   iterations = 30
   # Draw "iterations" number of squares, increasing the rotation for each to create a spiral pattern
   for i in range (iterations, 0, -1):
      # Alternate colors for each square
      turtle.color(colors[i%2])
      turtle.fillcolor(colors[i%2])
      # Increase rotation
      degrees = rotateAmount * degreeIncrement
      degreeIncrement += 1
      if( clockwise):
         degrees *= -1
      
      drawSquare(xPos, yPos, squareSize, degrees)

      if(not clockwise):
         left(rotateAmount)
      else:
         right(rotateAmount)

      # Decrease the size of the square for each iteration.
      # Uses fractions to a power in order to make the squares closer together as they get smaller
      squareSize = size * ((i-1) / iterations) ** 3

# Create four spirals with alternating rotations
colors = ["white", "black"]
drawSpiralSquare(200, 200, 400, True)
colors = ["black", "white"]
drawSpiralSquare(-200, 200, 400, False)
colors = ["white", "black"]
drawSpiralSquare(-200, -200, 400, True)
colors = ["black", "white"]
drawSpiralSquare(200, -200, 400, False)

done()