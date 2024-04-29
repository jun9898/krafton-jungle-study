import sys
import heapq
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)

res = 0
tmp = 0
while arr:
    tmp = tmp + heapq.heappop(arr)
    res += tmp

print(res)