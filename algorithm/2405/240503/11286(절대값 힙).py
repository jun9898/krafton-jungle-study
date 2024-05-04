import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
        continue
    heapq.heappush(heap, (abs(tmp), tmp))
