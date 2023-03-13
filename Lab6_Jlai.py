# Name: Joshua Lai
# Lab 6
# Completed 3/9/2022

import math
import random

# Task One
def TaskOne():
    input_sentence = input("Please enter a sentence: ")
    # split the sentence based on space
    sentence_split = input_sentence.split(" ")
    final_sentence = ""
    first = True
    # for each word in the split, add a "#" before it.
    # skip if this is the first word.
    for word in sentence_split:
        if(not first):
            final_sentence += "#"
        first = False
        final_sentence += word
    print (final_sentence)

    # TASK ONE OUTPUT:

    # Which task would you like to run? Type 1, 2, or 3: 1
    # Please enter a sentence: Good Morning CS2520
    # Good#Morning#CS2520

    # Which task would you like to run? Type 1, 2, or 3: 1
    # Please enter a sentence: Hello World! Python is fun!
    # Hello#World!#Python#is#fun!

# Task Two
def TaskTwo():
    list_one = []
    # create user-defined list
    while(True):
        inputNum = input("Please enter a number. Enter \"d\" when done: ")
        if(inputNum == "d"):
            break
        list_one.append(int(inputNum))
    print("Your list:", list_one)
    # using list comprehension
    list_two = [random.randrange(0, 51) for i in range(20)]
    print("Random list:", list_two)
    last = list_one[len(list_one) - 1]
    print("the last number of the first list is {0}.".format(last))
    list_one = reverse_list(list_one)
    print("The first list reversed is:", list_one)

    combined_list = list_one + list_two
    combined_list = sorted(combined_list)
    print("These two lists combined and sorted is:", combined_list)

# a method that simply reverses the inputed list by iterating over it backwards
def reverse_list(list):
    result = []
    for i in range(len(list)-1, -1, -1):
        result.append(list[i])
    return result

    # TASK TWO OUTPUT:

    # Which task would you like to run? Type 1, 2, or 3: 2
    # Please enter a number. Enter "d" when done: 5
    # Please enter a number. Enter "d" when done: 2
    # Please enter a number. Enter "d" when done: 21
    # Please enter a number. Enter "d" when done: 23
    # Please enter a number. Enter "d" when done: 13
    # Please enter a number. Enter "d" when done: 17
    # Please enter a number. Enter "d" when done: 8
    # Please enter a number. Enter "d" when done: 1
    # Please enter a number. Enter "d" when done: 12
    # Please enter a number. Enter "d" when done: 45
    # Please enter a number. Enter "d" when done: d
    # Your list: [5, 2, 21, 23, 13, 17, 8, 1, 12, 45]
    # Random list: [28, 26, 11, 19, 11, 31, 50, 38, 14, 48, 11, 34, 9, 8, 40, 12, 22, 48, 6, 18]
    # the last number of the first list is 45.
    # The first list reversed is: [45, 12, 1, 8, 17, 13, 23, 21, 2, 5]
    # These two lists combined and sorted is: [1, 2, 5, 6, 8, 8, 9, 11, 11, 11, 12, 12, 13, 14, 17, 18, 19, 21, 22, 23, 26, 28, 31, 34, 38, 40, 45, 48, 48, 50]

    # Which task would you like to run? Type 1, 2, or 3: 2
    # Please enter a number. Enter "d" when done: 5 
    # Please enter a number. Enter "d" when done: 4
    # Please enter a number. Enter "d" when done: 3
    # Please enter a number. Enter "d" when done: 2
    # Please enter a number. Enter "d" when done: 1
    # Please enter a number. Enter "d" when done: 99999
    # Please enter a number. Enter "d" when done: d
    # Your list: [5, 4, 3, 2, 1, 99999]
    # Random list: [32, 50, 18, 16, 35, 13, 11, 20, 50, 21, 37, 0, 14, 37, 43, 44, 8, 7, 13, 6]
    # the last number of the first list is 99999.
    # The first list reversed is: [99999, 1, 2, 3, 4, 5]
    # These two lists combined and sorted is: [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 13, 14, 16, 18, 20, 21, 32, 35, 37, 37, 43, 44, 50, 50, 99999]

# Task Three
def TaskThree():
    names = ("Winny", "Ada", "Lev", "Kay", "Jack", "Sam", "Mark")
    ages = [20, 18, 22, 16, 20, 18, 18]
    do_zip(names, ages)
    print()
    names = ("Jerry", "George", "#$(#&*$@)", "Logan", "Katie", "Kevin")
    ages = [45, 23, 9999999, 31, 8, 8]
    do_zip(names, ages)

def do_zip(names, ages):
    people = zip(names, ages)
    youngest = next(people)
    total_age = youngest[1]
    length = 1
    # a tuple to hold the values as they are generated
    zipped_tuple = (youngest,)
    # because a zip object is a generator, iterate through each value
    for person in people:
        total_age += person[1]
        length += 1
        zipped_tuple += person,
        if(person[1] < youngest[1]):
            youngest = person
    print("The youngest person is {0} at {1} years old.".format(youngest[0], youngest[1]))
    print("The average age is {0:.2f} years old.".format(total_age / length))

    zipped_tuple = list(zipped_tuple)
    # first sort by age, then sort by age in decending order.
    # The resultant tuple is thus sorted by age, with individuals of the same age
    # sorted by alphabetical order.
    zipped_tuple.sort(key = lambda element : element[0])
    zipped_tuple.sort(key = lambda element : element[1], reverse = True)
    zipped_tuple = tuple(zipped_tuple)

    print("Tuple sorted according to age and name:\n" + str(zipped_tuple))

    # TASK THREE OUTPUT:

    # Which task would you like to run? Type 1, 2, or 3: 3
    # The youngest person is Kay at 16 years old.
    # The average age is 18.86 years old.
    # Tuple sorted according to age and name:
    # (('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16))

    # The youngest person is Katie at 8 years old.
    # The average age is 1666685.67 years old.
    # Tuple sorted according to age and name:
    # (('#$(#&*$@)', 9999999), ('Jerry', 45), ('Logan', 31), ('George', 23), ('Katie', 8), ('Kevin', 8))

if __name__ == "__main__":
    # Task selector
    selection = int(
        input("Which task would you like to run? Type 1, 2, or 3: "))
    if (selection == 1):
        TaskOne()
    elif (selection == 2):
        TaskTwo()
    elif (selection == 3):
        TaskThree()