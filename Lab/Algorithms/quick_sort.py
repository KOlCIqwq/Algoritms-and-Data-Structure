import random

def quick_sort(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, low, high):
        pivot_index = random.randint(low, high)  # Select a random pivot
        swap(arr, pivot_index, high)  # Move pivot to the end
        pivot = arr[high]
        i = low - 1  # Place for swapping
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                swap(arr, i, j)
        swap(arr, i + 1, high)  # Place pivot in its correct position
        return i + 1

    def helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            helper(arr, low, pivot_index - 1)
            helper(arr, pivot_index + 1, high)

    helper(arr, 0, len(arr) - 1)
    return arr

# Example usage:
""" a = input("Enter numbers separated by spaces: ")
arr = list(map(int, a.split()))
print(quicksort(arr))
"""