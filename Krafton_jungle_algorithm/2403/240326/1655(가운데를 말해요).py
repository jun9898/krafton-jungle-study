import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
answer = []

for i in range(n):
    x = int(input())
    if len(left_heap) == len(right_heap):
        hq.heappush(left_heap, (-x, x))
    else:
        hq.heappush(right_heap, (x, x))
    if right_heap and left_heap[0][1] > right_heap[0][1]:
        min = hq.heappop(right_heap)[1]
        max = hq.heappop(left_heap)[1]
        hq.heappush(left_heap, (-min, min))
        hq.heappush(right_heap, (max, max))
    print(left_heap[0][1])


