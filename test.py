def lower_bound(A, value):
    """Trova il primo indice in cui A[idx] >= value"""
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

#a = list(map(int,input().split()))

#print(test(a))
#print(lower_bound(a, 3))

print(1 % 8)