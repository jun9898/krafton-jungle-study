import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap))
        continue
    heapq.heappush(heap, a)



