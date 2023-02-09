# Name: Joshua Lai
# Lab 3
# Completed 2/10/2022

# Task 1
def TaskOne():
    # Initialize values array
    values = [1] * 3

    # Get user input
    values[0] = input("Please input the first value: ")
    values[1] = input("Please input the second value: ")
    values[2] = input("Please input the third value: ")

    # Ask user for variable type
    userSelection = input(
        "What type of variable are these? (s for string, i for int, f for float): ")

    # Convert variable types based on the user's selection ("s" simply leaves the string as is)
    for i in range(len(values)):
        match userSelection:
            case "i":
                values[i] = int(values[i])
            case "f":
                values[i] = float(values[i])

    # TASK 1: SINGLE PIECE OF CODE TO FIND LARGEST
    if (values[0] > values[1] and values[0] > values[2]):
        largest = values[0]
    elif (values[1] > values[0] and values[1] > values[2]):
        largest = values[1]
    else:
        largest = values[2]

    # Print largest
    print("Largest value:", largest)

    # TEST OUTPUT:

    # Test 1:
    # Which task would you like to run? Type 1, 2, 3, or 4: 1
    # Please input the first value: hello
    # Please input the second value: how're you
    # Please input the third value: hoho
    # What type of variable are these? (s for string, i for int, f for float): s
    # Largest value: how're you

    # Test 2:
    # Which task would you like to run? Type 1, 2, 3, or 4: 1
    # Please input the first value: 420
    # Please input the second value: 351
    # Please input the third value: 530
    # What type of variable are these? (s for string, i for int, f for float): i
    # Largest value: 530

    # Test 3:
    # Which task would you like to run? Type 1, 2, 3, or 4: 1    
    # Please input the first value: -35.8
    # Please input the second value: -28
    # Please input the third value: -36.5
    # What type of variable are these? (s for string, i for int, f for float): f
    # Largest value: -28.0

# Task 2
def TaskTwo():
    count = int(input("please enter the number of items purchased: "))
    total = int(input("please enter the total cost: "))
    print("Average =", 0 if count == 0 else total/count)

    # TEST OUTPUT:

    # Test 1:
    # Which task would you like to run? Type 1, 2, 3, or 4: 2
    # please enter the number of items purchased: 23
    # please enter the total cost: 56
    # Average = 2.4347826086956523

    # Test 2:
    # Which task would you like to run? Type 1, 2, 3, or 4: 2
    # please enter the number of items purchased: 0
    # please enter the total cost: 23
    # Average = 0

# Task 3
def TaskThree():
    pass
    # TASK 3
    # CODE A:
    j = 1
    while j < 10:
        j += 2
        if j == 5:
            continue
            print(j, end=" ")
    # PREDICTION: I predict that this will not print anything.
    # OUTPUT: This did indeed print nothing.
    # EXPLANATION: The print statement is situated after the continue statement, meaning it can never be reached.

    print()

    # CODE B:
    for j in range(50):
        j += 2
        print(j, end=" ")
        if j == 15:
            break
    # PREDICTION: I predict that this will print 2 4 6 8 ... until it hits 50.
    # OUTPUT: 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # EXPLANATION: The "for in range" loop overwrites the value of j every iteration,
    # so the j += 2 simply adds two to this incrementing value. It breaks when it hits 15.

# Task 4
def TaskFour():
    number = int(input("Enter a number to check Prime or Not: "))
    i = 2
    count = 0
    while (i <= number / 2):
        if (number % i == 0):
            count += 1
            break
        i += 1
    if (count == 0):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

    # TEST OUTPUT:

    # Test 1:
    # Which task would you like to run? Type 1, 2, 3, or 4: 4
    # Enter a number to check Prime or Not: 71
    # 71 is a prime number.

    # Test 2:
    # Which task would you like to run? Type 1, 2, 3, or 4: 4
    # Enter a number to check Prime or Not: 119
    # 119 is not a prime number.

    # Test 3:
    # Which task would you like to run? Type 1, 2, 3, or 4: 4
    # Enter a number to check Prime or Not: 2
    # 2 is a prime number.

    # Test 4:
    # Which task would you like to run? Type 1, 2, 3, or 4: 4
    # Enter a number to check Prime or Not: 360
    # 360 is not a prime number.

    # Test 5:
    # Which task would you like to run? Type 1, 2, 3, or 4: 4
    # Enter a number to check Prime or Not: 7919
    # 7919 is a prime number.

# Task selector
selection = int(
    input("Which task would you like to run? Type 1, 2, 3, or 4: "))
if (selection == 1):
    TaskOne()
elif (selection == 2):
    TaskTwo()
elif (selection == 3):
    TaskThree()
elif (selection == 4):
    TaskFour()
