def quick_sort_median(arr):
    '''
    1. Calculate the pivot as the median of medians
    2. Move the pivot to the end of the array
    3. Partition the array, with left part those elements smaller than pivot and right part those elements greater than pivot
    4. Recursively call quicksort on the left and right part
    O(nlogn) n to iterate the array and logn to partition
    '''
    # Swap two elements
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # Move all the elements smaller than pivot to the left and all the elements greater than pivot to the right
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)
        swap(arr, i + 1, high)  # Place pivot in its correct position
        return i + 1

    # Calculate the median of subarray composed by 5 elements and calculate the median again 
    def median_of_medians(arr):
        n = len(arr)
        if n <= 5:
            return sorted(arr)[n // 2]
        medians = []
        for i in range(0, n, 5):
            group = arr[i:i + 5]
            medians.append(sorted(group)[len(group) // 2])
        return median_of_medians(medians)

    # Handles the partition and recursively call left and right
    def helper(arr, low, high):
        if low < high:
            # Find the median of medians as pivot
            pivot = median_of_medians(arr[low:high + 1])
            # Move the pivot to the end of the current subarray
            pivot_index = arr.index(pivot, low, high + 1)
            swap(arr, pivot_index, high)
            # Partition the array
            p = partition(arr, low, high)
            # Recursively sort the left and right parts
            helper(arr, low, p - 1)
            helper(arr, p + 1, high)

    helper(arr, 0, len(arr) - 1)
    return arr