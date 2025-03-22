import random
def helper(arr):
    lo,hi = 0,len(arr)-1
    quicksort_3way(arr,lo,hi)
def quicksort_3way(arr, lo, hi):
    '''
    We gonna divide the array into three parts: Those who are less than the pivot, those who are equal to the pivot and those who are greater than the pivot
    Keep a pointer to the start and the end of the array, we iterate on the array with i.
    Each time i is less than the pivot, we swap i with the start pointer and increment both pointers
    Each time i is greater than the pivot, we swap i with the end pointer and decrement the end pointer
    If i is equal to the pivot, we just increment i
    Here we do an example walkthrough:
    [3, 5, 2, 3, 8, 1, 3, 7, 3, 6, 2], pivot = 3, left = 0, right = 10
    i = 1. arr[1] > pivot, swap arr[1] with arr[right], right = 9, i = 1 [3, 2, 2, 3, 8, 1, 3, 7, 3, 6, 5]
    i = 1, arr[1] < pivot, swap arr[1] with arr[left], left = 1, i = 2 [2, 3, 2, 3, 8, 1, 3, 7, 3, 6, 5]
    ... Continue this process until i > right
    [2, 2, 1, 3, 3, 3, 3, 6, 7, 8, 5]
    Now we recursively sort the left and right sections [2, 2, 1] and [6, 7, 8, 5]
    Average Case:O(n log n). Worst Case: O(n²). 3-way is useful when there are many duplicate keys
    '''
    if lo >= hi:
        return

    # Randomly select a pivot and swap it with the first element
    pivot_index = random.randint(lo, hi)
    arr[lo], arr[pivot_index] = arr[pivot_index], arr[lo]
    pivot = arr[lo]
    
    # Initialize pointers for partitioning:
    # left: marks end of section with elements less than pivot
    # right: marks beginning of section with elements greater than pivot
    left = lo
    right = hi
    i = lo + 1

    # Partitioning process
    while i <= right:
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        else:
            i += 1

    # Recursively sort the sections with elements less than and greater than pivot
    quicksort_3way(arr, lo, left - 1)
    quicksort_3way(arr, right + 1, hi)

""" a = input("Enter numbers separated by spaces: ")
arr = list(map(int, a.split()))
quicksort_3way(arr,0,len(arr)-1)
print(arr) """