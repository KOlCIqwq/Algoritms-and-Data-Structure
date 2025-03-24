
def PigeonSort(arr):
    '''
        1. creates a list frequency similar o counting sort
        2. frequency will be a list of lists of the elements
        3. after creation of frequency, it is iterated once more moving 
           the elements back to the original list 
        4. arr in the first case is a list of int; in the second is a list of lists of which the first element is an int 
    '''
    frequency = {}
    #index=0
    sortedArr = []
    for item in arr:
        if item not in frequency:
            frequency[item]=[]
        frequency[item].append(item)
    for key in sorted(frequency.keys()):
        sortedArr.extend(frequency.get(key))
    return arr
    
'''a = input()
arr = list(map(int, a.split()))
print(arr)
print("----------")
PigeonSort(arr)
print(arr)'''

#trial of the pidgeon with array instead of a dictionary (a lot worse)
'''
min_val = min(arr)
max_val = max(arr)
size = max_val-min_val+1
count=[[] for _ in range(size)]
#index=0
sortedArr = []
for item in arr:
    count[item-min_val].append(item)
for hole in count:
    sortedArr.extend(hole)
return sortedArr
'''