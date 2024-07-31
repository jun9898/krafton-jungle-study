import sys; input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
upArr = [1] * n
downArr = [1] * n

for i in range(n-1):
    if arr[i] <= arr[i+1]:
        upArr[i+1] += upArr[i]
    if arr[i] >= arr[i+1]:
        downArr[i+1] += downArr[i]

print(max(max(upArr),max(downArr)))
