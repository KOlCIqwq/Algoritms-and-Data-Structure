# n ^ 2
def n2(arr):
    prevMax = 0
    out = [0,0]
    for i in range(len(arr)):
        for j in range(len(arr) - 1,i + 1,-1):
            tempDiff = arr[j] - arr[i]
            if tempDiff > prevMax:
                out[0] = i
                out[1] = j
    return out
# O(n) 
'''
1. The maxDifference will be the max element - minElement
2. So we initialize the minVal and its index, and keep track of the previous maxDifference
3. If the difference of the current - the minimum is bigger than the previous, we update the max
4. If the current is smaller than the minVal, we found a new minimum so change it
'''
def n(arr):
    minVal = arr[0]
    minIdx = 0
    prevMax = float('-inf')
    out = [-1,-1]
    for i in range(len(arr)):
        diff = arr[i] - minVal
        if diff > prevMax:
            prevMax = diff
            out = [minIdx,i]
        if arr[i] < minVal:
            minVal = arr[i]
            minIdx = i
    return out



a = input()
def toIntArray(arr):
    out = list(map(int,arr.split()))
    return out
arr = toIntArray(a)
#k = int(input())

#print(n2(arr))
print(n(arr))