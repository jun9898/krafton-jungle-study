import sys
input = sys.stdin.readline

n = int(input())

me = int(input())

arr = []
for i in range(n-1):
    arr.append(int(input()))

count = 0
if arr:
    while me <= max(arr):
        n = arr.index(max(arr))
        arr[n] -= 1
        me += 1
        count += 1
print(count)