# Name: Joshua Lai
# Lab 11
# Completed

from typing import List
from typing import Tuple

def quick_sort(arr : List[int], low : int, high : int):
    if(low < high):
        partition_result = partition(arr, low, high)
        partition_index = partition_result[0]
        arr = partition_result[1]
        arr = quick_sort(arr, low, partition_index - 1)
        arr = quick_sort(arr, partition_index + 1, high)
    return arr

# partition function, will use the element in arr[high] as pivot
# places all values smaller than pivot to left, all values larger than pivot to right
def partition(arr : List[int], low : int, high : int) -> Tuple[int, List[int]]:
    pivot = arr[high]
    # starting index of small values
    i = low - 1
    # iterate through arrary
    for j in range(low, high):
        # if we find a value smaller than pivot, swap it with our small index,
        # then increment the small index
        # this way, the left side of the array will be filled with smaller values
        if(arr[j] < pivot):
            i += 1
            arr = swap(arr, i, j)
    # place our pivot in the middle
    swap(arr, i + 1, high)
    return (i + 1, arr)

# simple swap function
def swap(arr : List[int], first_index : int, second_index : int) -> List[int]:
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp
    return arr

if __name__ == "__main__":
    test = [24, 53, 6, 75, 8, 9, 0, 34]
    print(test)
    test = quick_sort(test, 0, len(test) - 1)
    print(test)