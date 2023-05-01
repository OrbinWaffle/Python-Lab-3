# Name: Joshua Lai
# Lab 11
# Completed

from typing import List
from typing import Tuple

def main_one():
    integer_list = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    name_list = ["Kate", "Sam", "Kate", "Jolly", "Alp", "Beta", "Alpine", "Samuel", "Bob", "Joy"]
    tuple_list = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]

    integer_list = quick_sort(integer_list, compare_greater_than)
    print(integer_list)
    
    name_list = quick_sort(integer_list, compare_less_than)
    print(name_list)

    tuple_list = quick_sort(tuple_list, compare_tuple)
    print(tuple_list)

def compare_greater_than(first_val : any, second_val : any):
    return first_val > second_val

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

# quick sort function that passes in general values to the helper
def quick_sort(arr : List[any], func):
    return quick_sort_helper(arr, 0, len(arr) - 1, func)


# quick sort algorithm
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
    # starting index of small values
    i = low - 1
    # iterate through arrary
    for j in range(low, high):
        # if we find a value smaller than pivot, swap it with our small index,
        # then increment the small index
        # this way, the left side of the array will be filled with smaller values
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



def main_two():
    pass

if __name__ == "__main__":
    selection = int(input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        main_one()
    elif (selection == 2):
        main_two()