# Name: Joshua Lai
# Lab 2
# Completed 2/4/2022

# Task 1
def TaskOne():
   presentValue = float(input("Please enter the present value: "))
   interestRate = float(input("Please enter the interest rate: "))
   years = int(input("Please enter the number of years: "))

   # Future value calculation
   futureValue = presentValue * ((1+(interestRate/100)) ** years)

   # Formatted print to round to two decimals
   print("Future value: {:.2f}".format(futureValue))

   # Task 1 output

   # Test 1:
   # Which task would you like to run? Type 1, 2, or 3: 1
   # Please enter the present value: 1000
   # Please enter the interest rate: 5.0
   # Please enter the number of years: 30
   # Future value: 4321.94

   # Test 2:
   # Which task would you like to run? Type 1, 2, or 3: 1
   # Please enter the present value: 1530.50
   # Please enter the interest rate: 3.5
   # Please enter the number of years: 15
   # Future value: 2564.12

# Task 2
def TaskTwo():
   # Task 2 Part a
   v1, v2, v3 = 5, 2, 1
   v1 += 1
   v3 += v1 * (v2)
   v2 -= 1
   print("v1: {0}\nv2: {1}\nv3: {2}".format(v1, v2, v3))

   # Task 2 Part b (using same variables v1 v2 and v3)
   print("Swapping these three variables using tuple assignment:")
   
   # Switch values using tuple assignment
   v1, v2, v3 = v2, v3, v1

   print("v1: {0}\nv2: {1}\nv3: {2}".format(v1, v2, v3))

   # Task 2 output
   # Which task would you like to run? Type 1, 2, or 3: 2
   # v1: 6
   # v2: 1
   # v3: 13
   # Swapping these three variables using tuple assignment:
   # v1: 1
   # v2: 13
   # v3: 6

# Task 3
def TaskThree():
   numOne = int(input("Enter the value of num one: "))
   numTwo = int(input("Enter the value of num two: "))
   quotient = numOne // numTwo
   remainder = numOne % numTwo
   print("Quotient when {0}/{1} is: {2}".format(numOne, numTwo, quotient))
   print("Remainder when {0} is divided by {1} is: {2}".format(numOne, numTwo, remainder))

   # Task 3 output

   # Test 1:
   # Which task would you like to run? Type 1, 2, or 3: 3
   # Enter the value of num one: 12
   # Enter the value of num two: 35
   # Quotient when 12/35 is: 0
   # Remainder when 12 is divided by 35 is: 12

   # Test 2:
   # Which task would you like to run? Type 1, 2, or 3: 3
   # Enter the value of num one: 35
   # Enter the value of num two: 13
   # Quotient when 35/13 is: 2
   # Remainder when 35 is divided by 13 is: 9

# Task selector
selection = int(input("Which task would you like to run? Type 1, 2, or 3: "))
if(selection == 1):
   TaskOne()
elif(selection == 2):
   TaskTwo()
elif(selection == 3):
   TaskThree()