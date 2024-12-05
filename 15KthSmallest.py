def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]
# Move all the elements smaller than pivot to the left and all the elements greater than pivot to the right
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            swap(arr,i,j)
    swap(arr, i + 1, high)  # Place pivot in its correct position
    return i + 1

def quickSelect(arr,low,high,k):
    '''
    Calculate the pivot position inside the array, compare it to the k
    if k is the position we want return it
    if k is bigger than the pivot index, means the element we need to search is on the right part of the pivot
    if k is smaller, search in the left
    O(n^2) if pivot is at the end or start. O(n) if we select the pivot randomly
    '''
    if low == high:
        return arr[low]
    if k < 1 or k > len(arr):
        return None
    k = k - 1 # To 0 based
    while True:
        pivot = partition(arr,low,high)
        if pivot == k:
            return arr[pivot]
        if pivot < k: # Search the right part
            low = pivot + 1    
        if pivot > k: # Search left
            high = pivot - 1

import heapq
def heapSelect(arr,k):
    '''
    1. We create a minHeap using the elements of the array, import the heapq library (because the naming system I choosed can't import)
    2. Since the heapq uses a maxHeap as default, we convert the numbers into negative to obtain a minHeap
    3. Each time we insert the number and if the length of the heap is bigger than k we pop the largest element (root of the heap)
    4. The remaining root is the kth element
    O(n + klogk), n for the iteration, klogk for keeping the heap of k elements, the heapify costs [size]*log[size]
    '''
    minHeap = []
    for i in range(len(arr)):
        heapq.heappush(minHeap,-arr[i])
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return -minHeap[0] # Heapq stores maxHeap, we convert the numbers into negative to obtain a minHeap


def medianOfMedians(arr):
    n = len(arr)
    if n <= 5:
        return sorted(arr)[n//2]
    medians = []
    for i in range(0,n,5):
        group = arr[i:i + 5]
        medians.append(sorted(group)[len(group) // 2])
    return medianOfMedians(medians)

def quickSelectWithMedian(arr,low,high,k):
    '''
    1. Same as the quickSelect, but the pivot is the median of medians
    2. Each iteration we need to find the median of medians between low and high
    O(n) in worst and general case, due to the selection of the pivot
    '''
    if low == high:
        return arr[low]
    if k < 1 or k > len(arr):
        return None
    k = k - 1 # To 0 based
    while True:
        # Since we cut the array by 30%, we need to find new median of medians between high and low
        p = medianOfMedians(arr[low:high + 1])
        pivotIndex = arr.index(p,low,high + 1)
        swap(arr,pivotIndex,high)
        pivot = partition(arr,low,high)
        if pivot == k:
            return arr[pivot]
        if pivot < k: # Search the right part
            low = pivot + 1   
        if pivot > k: # Search left
            high = pivot - 1
a = list(map(int,input().split()))
k = int(input())

#print(quickSelect(a,0,len(a) - 1,k))
#print(heapSelect(a,k))
print(quickSelectWithMedian(a,0,len(a) - 1,k))
