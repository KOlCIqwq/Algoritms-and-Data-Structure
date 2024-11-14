# n ^ 3
def n3(arr,k):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            tempSum = 0
            for l in range(i,j+1):
                tempSum += arr[l]
            if tempSum == k:
                return [i,j]
    return (-1,-1)

# n: Using sliding window
'''
1. Init 2 indecex left and right, and a temporary sum
2. Iterate the array increamenting right each time
3. Increment the tempSum of current(arr[right]),each time check if its k 
4. In case its bigger, try to shrink the subarray subtracting left by 1 and tempSum by the leftmost element
# Can also be done with a prefix sum
# O(n) at worst case it iterate the full array of length n 
'''
def slidingWindow(arr,k):
    left = 0
    tempSum1 = arr[left]
    for right in range(1,len(arr)):
        tempSum1 += arr[right]
        while tempSum1 > k and left <= right:
            tempSum1 -= arr[left]
            left += 1
        if tempSum1 == k:
            return (left,right)
        
    return (-1,-1)

a = input()
def toIntArray(arr):
    out = list(map(int,arr.split()))
    return out
arr = toIntArray(a)
k = int(input())
#print(n3(arr,k))
print(slidingWindow(arr,k))

