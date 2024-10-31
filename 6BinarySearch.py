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
a = input()
k = int(input())
l = list(map(int, a.split()))
n = len(l)
print(binarySearch(l, k, 0, n))
