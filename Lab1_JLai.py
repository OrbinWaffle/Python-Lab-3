# Name: Joshua Lai
# Lab 1 - Task 2
# This program simulates a soda vending machine. It presents a menu,
# asks the user what drink they want to buy and how many, then outputs the final price.

# Arrays to store menu and price
sodas = ["Berry Blast", "Lemonade", "Yum Yum Cola"]
prices = [5, 3, 4]

print("Welcome to The Soda Machine. Here are the drinks available:")

# List of input characters that are valid
validSet = set("0123456789")

isValid = False
while(isValid == False):
   for index, item in enumerate(sodas):
         print("#" + str(index + 1), ":", item + ",", prices[index], "dollars")

   selection = input("Please enter the number of your selection: ")
   selectionNum = 0

   if(validSet.issuperset(selection)):
      selectionNum = int(selection) - 1
      if(selectionNum-1 >= 0 and selectionNum-1 < len(sodas)):
         isValid = True
         break

   print("\nInvalid selection. Please try again.")

print("\nYou selected", sodas[selectionNum] + ".")

isValid = False
while(isValid == False):
   cans = input("Input the number of cans you would like to purchase: ")
   numOfCans = 0

   if(validSet.issuperset(cans)):
      numOfCans = int(cans)
      isValid = True
      break
   print("\nInvalid input. Please try again.")

print("You purchased", numOfCans, "cans of", sodas[selectionNum] + ". Your total will be $" + str(numOfCans * prices[selectionNum]) + ".")

# Example Output:

# Welcome to The Soda Machine. Here are the drinks available:
# #1 : Berry Blast, 5 dollars
# #2 : Lemonade, 3 dollars
# #3 : Yum Yum Cola, 4 dollars
# Please enter the number of your selection: 2

# You selected Lemonade.
# Input the number of cans you would like to purchase: 4
# You purchased 4 cans of Lemonade. Your total will be $12.