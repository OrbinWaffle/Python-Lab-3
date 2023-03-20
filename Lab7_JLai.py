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
        if (len(text_dictionary) <= 0):
            quit()

def find_most_common(dict):
    most_common = list(dict.items())[0][0]
    for key in dict:
        if(dict[key] > dict[most_common]):
            most_common = key
    return most_common

# TASK ONE OUTPUT:
# Which task would you like to run? Type 1 or 2: 1
# Please type a sentence: python is an easy language python is easy to learn and easy to code a lot of python modules that are easy to use go python       
# {'PYTHON': 4, 'IS': 2, 'AN': 1, 'EASY': 4, 'LANGUAGE': 1, 'TO': 3, 'LEARN': 1, 'AND': 1, 'CODE': 1, 'A': 1, 'LOT': 1, 'OF': 1, 'MODULES': 1, 'THAT': 1, 'ARE': 1, 'USE': 1, 'GO': 1}
# Three most common words:
# "PYTHON" occurs a total of 4 times.
# "EASY" occurs a total of 4 times.
# "TO" occurs a total of 3 times.

# Which task would you like to run? Type 1 or 2: 1                 
# Please type a sentence: The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the 
# sound, your test is over. The test will begin on the word start. On your mark, get ready, start.
# {'THE': 8, 'FITNESSGRAM™': 1, 'PACER': 2, 'TEST': 5, 'IS': 2, 'A': 4, 'MULTISTAGE': 1, 'AEROBIC': 1, 'CAPACITY': 1, 'THAT': 1, 'PROGRESSIVELY': 1, 'GETS': 2, 'MORE': 1, 'DIFFICULT': 1, 'AS': 3, 'IT': 1, 'CONTINUES': 1, '20': 1, 'METER': 1, 'WILL': 2, 'BEGIN': 2, 'IN': 2, '30': 1, 'SECONDS': 1, 'LINE': 2, 'UP': 1, 'AT': 1, 'START': 3, 
# 'RUNNING': 1, 'SPEED': 1, 'STARTS': 1, 'SLOWLY': 1, 'BUT': 1, 'FASTER': 1, 'EACH': 2, 'MINUTE': 1, 'AFTER': 1, 'YOU': 3, 'HEAR': 2, 'THIS': 2, 'SIGNAL': 1, 'BEEP': 1, 'SINGLE': 1, 'LAP': 2, 'SHOULD': 1, 'BE': 1, 'COMPLETED': 1, 'TIME': 2, 'SOUND': 2, 'DING': 1, 'REMEMBER': 1, 'TO': 2, 'RUN': 2, 'STRAIGHT': 1, 'AND': 1, 'LONG': 1, 'POSSIBLE': 1, 'SECOND': 1, 'FAIL': 1, 'COMPLETE': 1, 'BEFORE': 1, 'YOUR': 2, 'OVER': 1, 'ON': 2, 'WORD': 1, 'MARK': 1, 'GET': 1, 'READY': 1}
# Three most common words:
# "THE" occurs a total of 8 times.
# "TEST" occurs a total of 5 times.
# "A" occurs a total of 4 times.

# Which task would you like to run? Type 1 or 2: 1
# Please type a sentence: Run run run! Run, Run@ #*RuN^ rUN! run. run... RUN! run- (run) run? run run? run RUN RUN!!!!!! $Run= rUn RuN ruN rUN; run: run. run run run. RUn??????? Run Run run& run. @#&^@#RUN#*$(#$& run. RUN Run~ run#*$& run, run, run, RUN---- run+ run= RUN. Run? Run... Run. Run. Run.
# {'RUN': 50}
# Three most common words:
# "RUN" occurs a total of 50 times.

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

# TASK TWO OUTPUT:
# Which task would you like to run? Type 1 or 2: 2
# Number of elements in either S1 or S2: 61 
# Number of elements in both S1 and S2: 28  
# Number of elements in S1 but not in S2: 33


# Task selector
if __name__ == "__main__":
    selection = int(
        input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        TaskOne()
    elif (selection == 2):
        TaskTwo()