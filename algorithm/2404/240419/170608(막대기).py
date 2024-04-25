import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

res = 0

max = 0
for i in range(n-1, -1, -1):
    if arr[i] > max:
        res += 1
        max = arr[i]

print(res)
