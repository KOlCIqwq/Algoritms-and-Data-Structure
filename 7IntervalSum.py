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
# Max-interval
def buildSegmentTree(arr):
    n = len(arr)
    # Height of segment tree
    height = (n - 1).bit_length()
    # Maximum size of segment tree
    max_size = 2 * (2 ** height) - 1
    tree = [0] * max_size

    def build(node, start, end):
        if start == end:
            # Leaf node will have a single element
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

    build(0, 0, n - 1)
    return tree

def querySegmentTree(tree, n, L, R):
    def query(node, start, end, L, R):
        if R < start or end < L:
            return float('-inf')  # Out of range
        if L <= start and end <= R:
            return tree[node]  # Current segment is completely within range
        mid = (start + end) // 2
        left_max = query(2 * node + 1, start, mid, L, R)
        right_max = query(2 * node + 2, mid + 1, end, L, R)
        return max(left_max, right_max)

    return query(0, 0, n - 1, L, R)

def maxInterval(arr, intervals):
    n = len(arr)
    tree = buildSegmentTree(arr)

    results = []
    for l in range(0,len(intervals),2):
        r = l + 1
        results.append(querySegmentTree(tree, n, l, r))
    
    return results

#a = input()
#b = input()
#arr = list(map(int,a.split()))
#intervals = list(map(int,b.split()))
a = [5, 0, 3, 1, 13, 7, 5]
b = [0, 6, 2, 4, 3, 6]
print(easySum(a,b))           
print(midSum(a,b))
print(maxInterval(a,b))
