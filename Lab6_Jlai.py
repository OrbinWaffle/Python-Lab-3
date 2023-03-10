# Name: Joshua Lai
# Lab 6
# Completed 3/9/2022

import math
import random

# Task One
def TaskOne():
    input_sentence = input("Please enter a sentence: ")
    sentence_split = input_sentence.split(" ")
    final_sentence = ""
    first = True
    for word in sentence_split:
        if(not first):
            final_sentence += "#"
        first = False
        final_sentence += word
    print (final_sentence)
# Task Two
def TaskTwo():
    list_one = []
    while(True):
        inputNum = input("Please enter a number. Enter \"d\" when done: ")
        if(inputNum == "d"):
            break
        list_one.append(int(inputNum))
    print("Your list:", list_one)
    list_two = [random.randrange(0, 51) for i in range(20)]
    print("Random list:", list_two)
    last = list_one[len(list_one) - 1]
    print("the last number of the first list is {0}.".format(last))
    list_one = reverse_list(list_one)
    print("The first list reversed is:", list_one)

    combined_list = list_one + list_two
    combined_list = sorted(combined_list)
    print("These two lists combined and sorted is:", combined_list)

def reverse_list(list):
    result = []
    for i in range(len(list)-1, -1, -1):
        result.append(list[i])
    return result

# Task Three
def TaskThree():
    pass
# Task Four
def TaskFour():
    pass
# Task Five
def TaskFive():
    pass

# Task selector
selection = int(
    input("Which task would you like to run? Type 1, 2, 3, 4, or 5: "))
if (selection == 1):
    TaskOne()
elif (selection == 2):
    TaskTwo()
elif (selection == 3):
    TaskThree()
elif (selection == 4):
    TaskFour()
elif (selection == 5):
    TaskFive()