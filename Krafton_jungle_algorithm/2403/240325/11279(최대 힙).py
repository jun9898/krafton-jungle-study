import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x= int(input())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)
