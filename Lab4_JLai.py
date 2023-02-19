# Name: Joshua Lai
# Lab 4
# Completed 2/20/2022

import math

# Task One
def TaskOne():
    sum1 = sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    sum2 = math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    print("Sum using sum(): {0}\nSum using fsum(): {1}".format(sum1, sum2))

# Task Two
def TaskTwo():
    print(task2())
def task2() :
    for i in range (8) :
        print(i, end = ' ')

# Task Three
def TaskThree():
    # Will print 18
    print(hoho(5))

    # Will also print 18
    print(hoho(6,z=3,y=1))

# def fun (x = 1, y = 2, z):
#     z = x + y
#     y += 1
#     return z*y

# Error: "x" and "y" have default values, but the "z" variable does not.

def hoho (x, y = 2, z=1):
    z = x + z
    y += 1
    return z*y
# Valid function

# Task Four
def TaskFour():
    main4()
def main4() :
    z, y = 3, 4
    print(z, y)
    z, y = swap(z, y)
    print(z, y)

    x, w = "hi", "ho"
    print(x, w)
    x, w = swap(x, w)
    print(x, w)

    v, u = True, False
    print(v, u)
    v, u = swap(v, u)
    print(v, u)

def swap(a, b):
    return b, a

# Task Five
def TaskFive():
    main5()
a, b = 0, 5
def main5() :
    global a, b
    i = 10
    b = g(i)
    print(a+b+i)
def f(i) :
    n=0
    while n*n <= i:
        n = n + 1
    return n-1
def g(a) :
    b=0
    for n in range(a):
        i = f(n)
        b = b+i
        return b

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