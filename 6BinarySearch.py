a = input()
l = list(map(int,a.split(' ')))
k = int(input())
n = len(l)
mid = n // 2
while l[mid] != k and mid < n and mid > 0:
          if l[mid] > k:
                  mid = mid // 2
          else:
                  mid = (mid + (mid//2)) // 2
if l[mid] == k:
        print(mid)
else:
        print(-1)