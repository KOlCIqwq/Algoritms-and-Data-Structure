# Optimal O(n + n) 
'''
1.Loop n times to find the element that occurs most of the times
loop the array to find how many times it occurs and check if it corrisponds to n // 2 
'''
def majorityElement(arr):
    count = 0
    m = -1
    for c in arr:
        if count == 0:
            m = c
            count += 1
        elif c != m:
            count -= 1
        else:
            count += 1
    times = 0
    for i in arr:
        if i == m:
            times += 1
    if times <= len(arr) // 2:
        return "No Majority"
    return m

a = input()
def toIntArray(arr):
    out = list(map(int,arr.split()))
    return out
arr = toIntArray(a)

print(majorityElement(arr))