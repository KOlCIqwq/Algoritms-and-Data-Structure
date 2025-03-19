def countingsort(arr):
    # Count frequency of each element using a dictionary.
    frequency = {}
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1

    # Get the sorted list of unique keys.
    sorted_keys = sorted(frequency)
    
    # Compute cumulative counts to determine positions.
    cum_count = {}
    total = 0
    for key in sorted_keys:
        total += frequency[key]
        cum_count[key] = total

    # Create an output array of the same length.
    output = [None] * len(arr)
    
    # Place each element in the correct position by iterating backwards.
    # This reverse traversal ensures that elements with equal keys maintain
    # their original relative order (stability).
    for item in reversed(arr):
        pos = cum_count[item] - 1
        output[pos] = item
        cum_count[item] -= 1

    return output

a = input()
arr = list(map(int, a.split()))

print(countingsort(arr))