# Name: Joshua Lai
# Lab 7
# Completed 3/20/2022

import string
import random
import os

# Task One

def TaskOne():
    # Get file path using current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Open file
    file = open(dir_path + "\\we_cant_touch.txt", "r")

    # Read file into lines list
    lines = file.readlines()
    print(lines[0].rstrip("\n"))
    print(lines[2].rstrip("\n"))
    # Close file
    file.close()

    print()

    # Open file
    file = open(dir_path + "\\we_cant_touch.txt", "r")

    line_list = []
    # Iterate through lines in file, appending them into the list
    for line in file:
        line_list.append(line)
    print(line_list[1].rstrip("\n"))
    print(line_list[3].rstrip("\n"))

    # Which task would you like to run? Type 1, 2, or 3: 1
    # We canâ€™t touch
    # We hunker down

    # But we still reach out
    # But we still rise up

# Task Two


def TaskTwo():
    # write strings one by one, i.e. write(str)
    fp = open('data1.txt', 'w')
    fp.write("BILL:\tHello, ")
    fp.write("how are you?")
    fp.write("\n")
    fp.write("BOB:\tI'm good.\n")
    fp.write("BILL:\tThat's good.\n")
    fp.write("BOB:\tThank you.\n")
    fp.write("BILL:\tBye.\n")
    fp.write("BOB:\tSo long.\n")
    fp.close()
    # writelines(): write a sequence, i.e. a list or a tuple into a file
    fp = open('data2.txt', 'w')
    fp.writelines(["BILL:\tHello, ", "how are you?", "\n", "BOB:\tI'm good.\n", "BILL:\tThat's good.\n", "BOB:\tThank you.\n", "BILL:\tBye.\n", "BOB:\tSo long.\n"])
    fp.close()

    # OUTPUT FOR BOTH OF THESE METHODS:
    # BILL:	Hello, how are you?
    # BOB:	I'm good.
    # BILL:	That's good.
    # BOB:	Thank you.
    # BILL:	Bye.
    # BOB:	So long.

def TaskThree():
    # Loop till we get valid input
    while True:
        # Ask whether or not to use relative path
        user_input = input("Is the file in the current directory? y/n, or q to quit: ")
        file_path = ""
        if(user_input == "y"):
            file_name = input("Please input the file name: ")
            # Add current directory to file path
            file_path = os.path.dirname(os.path.realpath(__file__)) + "\\" + file_name
        elif(user_input == "q"):
            exit()
        else:
            file_path = input("Please input the direct path to the file: ")
        # Attempt to open file
        try:
            file = open(file_path, "r")
            break
        # If file open fails, print error and try again
        except (PermissionError, FileNotFoundError):
            print("Error: Could not find file at path {0} Please try again.\n".format(file_path))
    float_list = []
    for line in file:
        # For each line, try to convert to float
        try:
            float_val = float(line)
        # If conversion fails, set to 0.0
        except ValueError:
            float_val = 0.0
        float_list.append(float_val)
    print(float_list)
        
    # Which task would you like to run? Type 1, 2, or 3: 3
    # Is the file in the current directory? y/n, or q to quit: y
    # Please input the file name: numbers.txt
    # [102.0, 99999.0, 20.5, 90.0, 0.0, 0.0, 2370.3887, 0.0, 0.1, 0.0, 30.2, 0.0, 0.2384234]

# Task selector
if __name__ == "__main__":
    selection = int(
        input("Which task would you like to run? Type 1, 2, or 3: "))
    if (selection == 1):
        TaskOne()
    elif (selection == 2):
        TaskTwo()
    elif (selection == 3):
        TaskThree()
