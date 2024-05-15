import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [1] * (m+1)

for i in range(2, m+1):
    if arr[i] == 1:
        tmp = i
        for j in range(i*2, m+1, tmp):
            arr[j] = 0

for i in range(n, m+1):
    if i == 1:
        continue
    if arr[i] == 1:
        print(i)
