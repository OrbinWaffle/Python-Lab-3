# Name: Joshua Lai
# Lab 7
# Completed 3/20/2022

import string
import random
import os

# Task One
def TaskOne():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(dir_path + "\\text_file.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line)
    print(line_list[0])
    print(line_list[1])
    print(line_list[2])
    print(line_list[3])

# Task Two
def TaskTwo():
    pass

# Task selector
if __name__ == "__main__":
    selection = int(
        input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        TaskOne()
    elif (selection == 2):
        TaskTwo()