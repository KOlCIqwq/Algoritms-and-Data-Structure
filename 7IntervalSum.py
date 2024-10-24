#a = input()
#b = input()
a = [5, 0, 3, 1, 13, 7, 5]
b = [0, 6, 2, 4, 3, 6]
#arr = list(map(int,a.split(' ')))
#intervals = list(map(int,a.split(' ')))

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
print(easySum(a,b))

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
print(midSum(a,b))
