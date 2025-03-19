import random

def quick_sort_3way(arr, m=None):
    def _quick_sort_3way(low, high):
        if low >= high:
            return
        pivot = arr[random.randint(low, high)]
        lt, i, gt = low, low, high
        while i <= gt:
            if arr[i] < pivot:
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        _quick_sort_3way(low, lt - 1)
        _quick_sort_3way(gt + 1, high)
    _quick_sort_3way(0, len(arr)-1)

a = input()
arr = list(map(int, a.split()))

print(quick_sort_3way(arr))