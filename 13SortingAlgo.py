def mergeSort(arr):
    '''
    1. Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
    2. Merge the sublists to produce a sorted list
    3. When merging 2 arrays when one of the arrays is empty, we just append the remaining elements of the other array
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0 # Index to left, right and arr

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left, if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right, if any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr 
def quicksort(arr):
    def swap(arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low,high):
            if arr[j] <= pivot:
                i += 1
                swap(arr,i,j)
        swap(arr, i + 1, high)  # Place pivot in its correct position
        return i + 1
    
    def median_of_medians(arr):
        n = len(arr)
        if n <= 5:
            return sorted(arr)[n//2]
        medians = []
        for i in range(0,n,5):
            group = arr[i:i + 5]
            medians.append(sorted(group)[len(group) // 2])
        return median_of_medians(medians)
    def helper(arr,low,high):
        if low < high:
            # Find the median of medians as pivot
            pivot = median_of_medians(arr[low:high + 1])
            # Move the pivot to the end of the current subarray
            pivot_index = arr.index(pivot)
            swap(arr, pivot_index, high)
            # Partition the array
            pi = partition(arr, low, high)
            # Recursively sort the left and right parts
            helper(arr, low, pi - 1)
            helper(arr, pi + 1, high)
    helper(arr,0,len(arr) - 1)
    return arr



a = input()
arr = list(map(int, a.split()))

print(mergeSort(arr))
print(quicksort(arr))