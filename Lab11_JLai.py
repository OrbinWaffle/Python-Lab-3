# Name: Joshua Lai
# Lab 11
# Completed 5/2/2023

from typing import List
from typing import Tuple
from math import sqrt

def main_one():
    integer_list = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    name_list = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"]
    tuple_list = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]

    integer_list = quick_sort(integer_list, compare_greater_than)
    name_list = quick_sort(name_list, compare_less_than)
    tuple_list = quick_sort(tuple_list, compare_tuple)

    print("Numbers in descending order:\n" + str(integer_list) + "\n")
    print("Names in alphabetical order: \n" + str(name_list) + "\n")
    print("Tuples sorted by alphabetical name, then by decending number:\n" + str(tuple_list) + "\n")

# returns true if first_val > second_val
def compare_greater_than(first_val : any, second_val : any):
    return first_val > second_val

# returns true if first_val < second_val
def compare_less_than(first_val : any, second_val : any):
    return first_val < second_val

# tuple comparator. First evaluate by the string. If the string is the same, evaluate by the int.
def compare_tuple(first_val : Tuple[str, int], second_val : Tuple[str, int]):
    if(first_val[0] < second_val[0]):
        return True
    elif (first_val[0] > second_val[0]):
        return False
    else:
        if(first_val[1] > second_val[1]):
            return True
        else:
            return False

# quick sort function that passes in start/end values to the helper
def quick_sort(arr : List[any], func):
    return quick_sort_helper(arr, 0, len(arr) - 1, func)

# generic quick sort algorithm
# takes in a list, start/end values, and a comparision function
def quick_sort_helper(arr : List[any], low : int, high : int, func):
    if(low < high):
        # partition based on high index
        partition_result = partition(arr, low, high, func)
        partition_index = partition_result[0]
        arr = partition_result[1]
        # call quick sort on the two partitioned halves
        arr = quick_sort_helper(arr, low, partition_index - 1, func)
        arr = quick_sort_helper(arr, partition_index + 1, high, func)
    return arr

# partition function, will use the element in arr[high] as pivot
# places all values smaller than pivot to left, all values larger than pivot to right
def partition(arr : List[int], low : int, high : int, func) -> Tuple[int, List[any]]:
    pivot = arr[high]
    # starting index of lefthand values
    i = low - 1
    # iterate through arrary
    for j in range(low, high):
        # compare using the function passed in earlier. If true, swap the values with the first available lefthand slot
        if(func(arr[j], pivot)):
            i += 1
            arr = swap(arr, i, j)
    # place our pivot in the middle
    swap(arr, i + 1, high)
    return (i + 1, arr)

# simple swap function
def swap(arr : List[int], first_index : int, second_index : int) -> List[any]:
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp
    return arr

# TASK ONE OUTPUT:

# Which task would you like to run? Type 1 or 2. Type q to quit: 1
# Numbers in descending order:
# [22, 17, 13, 12, 9, 6, 5, 4, 2, 1]

# Names in alphabetical order:
# ['Alp', 'Alpine', 'Beta', 'Bob', 'Jolly', 'Joy', 'Kate', 'Kate', 'Sam', 'Samuel']

# Tuples sorted by alphabetical name, then by decending number:
# [('Alp', 2), ('Alp', 1), ('Alpine', 2), ('Beta', 3), ('Bob', 2), ('Jolly', 1), ('Kate', 5), ('Kate', 3), ('Sam', 4), ('Sam', 3), ('Sam', 2)]


# Which task would you like to run? Type 1 or 2. Type q to quit: q

def main_two():
    # using list comprehension
    ordered_list = [x for x in range(1, 101)]
    
    # for each element in the list, double it
    doubled_list = list(map(lambda x : x*2, ordered_list))

    # for each element in the list, if it is odd, square it
    squared_list = list(map(lambda y : y**2, filter(lambda x : x % 2 == 1, ordered_list)))

    # for each element in list, if isPrime returns true, keep it
    prime_list = list(filter(isPrime, ordered_list))

    print("List of integers from 1 to 100:\n" + str(ordered_list) + "\n")
    print("List of doubles of the integers from 1 to 100:\n" + str(doubled_list) + "\n")
    print("List of squares of the odd integers from 1 to 100:\n" + str(squared_list) + "\n")
    print("List of primes from 1 to 100\n" + str(prime_list) + "\n")

def isPrime (n) :
    if n <= 1 :
        return 0
    for fac in range (2, int(sqrt(n))+1) :
        if n % fac == 0 :
            return 0
    return 1

# TASK TWO OUTPUT:

# Which task would you like to run? Type 1 or 2. Type q to quit: 2
# List of integers from 1 to 100:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 
# 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 
# 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# List of doubles of the integers from 1 to 100:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

# List of squares of the odd integers from 1 to 100:
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025, 2209, 2401, 2601, 2809, 3025, 3249, 3481, 3721, 3969, 4225, 4489, 4761, 5041, 5329, 5625, 5929, 6241, 6561, 6889, 7225, 7569, 7921, 8281, 8649, 9025, 9409, 9801]

# List of primes from 1 to 100
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Which task would you like to run? Type 1 or 2. Type q to quit: q

if __name__ == "__main__":
    while(True):
        try:
            selection = input("Which task would you like to run? Type 1 or 2. Type q to quit: ")
            if (selection == "q"):
                quit()
            if (int(selection) == 1):
                main_one()
            elif (int(selection) == 2):
                main_two()
        except ValueError:
            print("Invalid input.")
        print()