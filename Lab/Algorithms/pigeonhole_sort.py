def PigeonSort(arr):
    '''
        1. creates a list frequency similar o counting sort
        2. frequency will be a list of lists of the elements
        3. after creation of frequency, it is iterated once more moving 
           the elements back to the original list 
        4. arr in the first case is a list of int; in the second is a list of lists of which the first element is an int 
    '''
    frequency = {}
    index=0
    for item in arr:
        if item not in frequency:
            frequency[item]=[]
        frequency[item].append(item)
    for key in sorted(frequency.keys()):
        for element in frequency[key]:
            arr[index]=element
            index+=1
            
a = input()
arr = list(map(int, a.split()))
print(arr)
print("----------")
PigeonSort(arr)
print(arr)