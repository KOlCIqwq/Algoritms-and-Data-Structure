def easySum(arr,intervals) -> int:
        n = len(arr)
        out = []
        for i in range(0,len(intervals),2):
                sum = 0
                left = intervals[i]
                right = intervals[i + 1]
                
                if left > right or left > n or right > n:
                          return 
                for j in range(left,right + 1):
                          sum += arr[j]
                out.append(sum)
        return out

def midSum(arr,intervals) -> int:
        n = len(arr)
        out = []
        contArray = [0]
        sum = 0
        for i in range(n):
                sum += arr[i]
                contArray.append(sum)
        for i in range(0,len(intervals),2):
                left = intervals[i]
                right = intervals[i + 1] + 1
                if left > right or left > n or right > n:
                          return 
                out.append(contArray[right] - contArray[left])     
        return out

class Segment:
    def __init__(self,i,j,left,right,val):
        self.i = i
        self.j = j
        self.left = left
        self.right = right
        self.val = val

def transformToTree(arr,i,j):

    assert (i <= j)
    
    if j == i + 1: # 1 element
        return Segment(i,j,None,None,a[i])
    if i == j: # Empty
        return None
    k = (i + j) // 2
    left = transformToTree(arr,i,k)
    right = transformToTree(arr,k,j)
    return Segment(i,j,left,right,max(left.value,right.value))

def prefix(s,i,j): # Get the node that starts exactly with i, and p.j not over j
    
    assert(i < j)
    assert(s.i <= i)
    
    if s.i == i and s.j <= j:
        return s
    if i < s.left.i:
        return prefix(s.left,i,j)
    else:
        return prefix(s.right,i,j)

def getMax(seg,i,j):
    
    assert(i <= j)
    
    if i == j:
        return float('-inf')
    p = prefix(seg,i,j)
    return max(p.val, getMax(seg,p.j,j))


#a = input()
#b = input()
#arr = list(map(int,a.split()))
#intervals = list(map(int,b.split()))
a = [5, 0, 3, 1, 13, 7, 5]
b = [0, 6, 2, 4, 3, 6]

segment = transformToTree(a)

print(easySum(a,b))           
print(midSum(a,b))

for k in range(0,len(b),2):
    i = b[k]
    j = b[k + 1]
    print(getMax(segment,i,j + 1))

