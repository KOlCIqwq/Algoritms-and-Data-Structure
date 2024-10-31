# n ^ 2
def n2(a,k):
    for i in range(len(a)):
        first = a[i]
        for j in range(i + 1,len(a)):
            temp = first + a[j]
            if temp == k:
                return [i,j]
    return [-1,-1]

# nlogn
def binarySearch(l, k, i, j):
    if i >= j:
        return -1
    mid = i + (j - i) // 2 
    if l[mid] == k:
        return mid
    elif l[mid] < k:
        return binarySearch(l, k, mid + 1, j)
    else:
        return binarySearch(l, k, i, mid)
def nlogn(a,k):
    small,big = 0,len(a)
    while small <= big:
        if small == big:
            return [-1,-1]
        comp = k - a[small]
        compIdx = binarySearch(a,comp,small,big)
        if compIdx == -1:
            small += 1
            continue
        else:
            return [small,compIdx]

def n(a,k):
    l,r = 0,len(a) - 1
    while l < r:
        temp = a[l] + a[r]
        if temp == k:
            return [l,r]
        elif temp < k:
            l += 1
        elif temp > k:
            r -= 1
    return [-1,-1]
a = [3, 7, 8, 11, 15, 20, 24]
k = 23
b = input()
a = list(map(int,b.split()))
k = int(input())
print(n(a,k))