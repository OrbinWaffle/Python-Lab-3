# Name: Joshua Lai
# Lab 7
# Completed 3/20/2022

import string
import random

# Task One
def TaskOne():
    text = input("Please type a sentence: ")
    # remove punctuation
    for i in string.punctuation:
        text = text.replace(i, "")
    # make all uppercase
    text = text.upper()

    split_text = text.split(" ")
    text_dictionary = dict.fromkeys(split_text, 0)
    for word in split_text:
        text_dictionary[word] += 1
    print(text_dictionary)
    print("Three most common words:")
    for i in range(3):
        most_common = find_most_common(text_dictionary)
        print("\"{0}\" occurs a total of {1} times.".format(most_common, text_dictionary[most_common]))
        del text_dictionary[most_common]

def find_most_common(dict):
    most_common = list(dict.items())[0][0]
    for key in dict:
        if(dict[key] > dict[most_common]):
            most_common = key
    return most_common

# Task Two
def TaskTwo():
    L1 = [random.randrange(1, 101) for i in range(0, 100)]
    L2 = [num for num in L1 if (num % 3 == 0 or num % 4 == 0)]

    S1 = set(L1)
    S2 = frozenset(L2)

    R1 = set(set().union(S1, S2))
    R2 = set(num for num in S1 if (num in S2))
    R3 = set(num for num in S1 if (not num in S2))

    print("Number of elements in either S1 or S2:", len(R1))
    print("Number of elements in both S1 and S2:", len(R2))
    print("Number of elements in S1 but not in S2:", len(R3))


# Task selector
if __name__ == "__main__":
    selection = int(
        input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        TaskOne()
    elif (selection == 2):
        TaskTwo()