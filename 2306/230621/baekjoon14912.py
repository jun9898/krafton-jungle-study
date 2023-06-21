from collections import Counter
n, m = map(int,input().split())

arr = []
for i in range(1,n+1):
    arr.extend(str(i))

arr = Counter(arr)

print(arr[str(m)])