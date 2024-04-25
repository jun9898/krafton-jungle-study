import sys
import heapq
input = sys.stdin.readline

n = int(input())

queue = []
for i in range(n):
    heapq.heappush(queue, int(input()))

res = []
while len(queue) >= 2:
    tmp1 = heapq.heappop(queue)
    tmp2 = heapq.heappop(queue)
    res.append(tmp1+tmp2)
    heapq.heappush(queue, tmp1+tmp2)

print(sum(res))

