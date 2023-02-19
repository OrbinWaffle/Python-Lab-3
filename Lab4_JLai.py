# Name: Joshua Lai
# Lab 4
# Completed 2/20/2022

import math

# Task One
def TaskOne():
    sum1 = sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    sum2 = math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    print("Sum using sum(): {0}\nSum using fsum(): {1}".format(sum1, sum2))

    # sum will print out 0.9999999999999999, while fsum prints out 1.0.
    # This is because there are floating point accuracy limitations with the standard sum().
    # fsum is designed to add floats and has a higher accuracy. Thus, it prints out the intended 1.0.

# Task Two
def TaskTwo():
    print(task2())
def task2() :
    for i in range (8) :
        print(i, end = ' ')

    # When we attempt to print task2(), it runs the method and then tries to print what it returns.
    # Because there is nothing returned, it prints "None" instead.

# Task Three
def TaskThree():
    
    # def fun (x = 1, y = 2, z):
    #     z = x + y
    #     y += 1
    #     return z*y

    # Error: "x" and "y" have default values assigned, but the "z" variable does not.
    # Python requires that once a default value is assigned, all subsequent parameters must also have default values.

    def hoho (x, y = 2, z=1):
        z = x + z
        y += 1
        return z*y
    # Valid function. x does not require a default value since there are no default values assigned before it.
    # The first parameter with a default value assigned is y, and all subsequent parameters have default values.

    print(hoho(5))
    # Will print 18.
    # 5 + 1 = 6
    # 2 + 1 = 3
    # 6 * 3 = 18

    print(hoho(6,z=3,y=1))
    # Will also print 18.
    # 6 + 3 = 9
    # 1 + 1 = 2
    # 9 * 2 = 18

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

    # The original function does not work.
    # This is becuase the parameters passed in are not actually references to the original variables.
    # Instead, they are local copies of the variables. Therefore, modifying them does not change the original values.
    # To fix this, I changed the function to return the parameters, but swapped.

# Task Five
def TaskFive():
    main5()
# a and b have global scope
a, b = 0, 5
def main5() :
    global a, b
    # i is local to main5()
    i = 10
    # call g(10)
    b = g(i)
    # g(10) returns 0
    # 0 + 0 + 10 = 10
    print(a+b+i)
def f(i) :
    # n is local to f()
    n=0
    # called f(0), so i = 0
    # 0 * 0 <= 0, so increment n
    # 1 * 1 > 0, so exit loop
    while n*n <= i:
        n = n + 1
    # n = 1, so returns 0
    return n-1
def g(a) :
    # b shadows the original global b and is treated as a local variable
    b=0
    # a shadows the original global a and is treated as a local variable
    for n in range(a):
        # first iteration: n = 0
        # i is local to g()
        # call f(0)
        i = f(n)
        # f(0) returns 0
        # b = 0, so b + 0 = 0
        b = b+i
        # Because of this return, the loop is only executed once
        # return 0
        return b

    # GUESS: The progarm will print out 10
    # ACTUAL: The program prints out 10

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