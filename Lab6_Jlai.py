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

# Task Three
def TaskThree():
    names = ("Winny", "Ada", "Lev", "Kay", "Jack", "Sam", "Mark")
    ages = [20, 18, 22, 16, 20, 18, 18]
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