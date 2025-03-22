def counting_sort(arr):
    '''
    Find the minimum and maximum values in the array, then create a table holding the range of these values
    Count them and insert to the table, and then place these number backwards to hold the original position (stable)
    '''
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

""" a = input("Enter numbers separated by spaces: ")
arr = list(map(int, a.split()))
print(counting_sort(arr)) """
