import random

def iterative_quick_sort(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, low, high):
        pivot_index = random.randint(low, high)  # Select a random pivot
        swap(arr, pivot_index, high)  # Move pivot to the end
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                swap(arr, i, j)
        swap(arr, i + 1, high)
        return i + 1

    # Stack to simulate recursion
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))  # Left side
            stack.append((pivot_index + 1, high))  # Right side
    return arr


def iterative_quick_sort_median(arr):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)
        swap(arr, i + 1, high)
        return i + 1

    def median_of_medians(arr):
        n = len(arr)
        if n <= 5:
            return sorted(arr)[n // 2]
        medians = [sorted(arr[i:i+5])[len(arr[i:i+5]) // 2] for i in range(0, n, 5)]
        return median_of_medians(medians)

    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = median_of_medians(arr[low:high + 1])
            pivot_index = arr.index(pivot, low, high + 1)
            swap(arr, pivot_index, high)
            p = partition(arr, low, high)
            stack.append((low, p - 1))  # Left side
            stack.append((p + 1, high))  # Right side
    return arr

# Example usage:
""" a = input("Enter numbers separated by spaces: ")
arr = list(map(int, a.split()))
print(iterative_quick_sort(arr))
print(iterative_quick_sort_median(arr)) """