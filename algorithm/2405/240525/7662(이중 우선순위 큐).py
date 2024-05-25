import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    heap_max = []
    heap_min = []
    heap_dict = defaultdict(int)
    k = int(input())

    def clear(heap, k=1):
        while heap and not heap_dict[heap[0] * k]:
            heapq.heappop(heap)

    for _ in range(k):
        command, value = input().rstrip().split()
        value = int(value)
        if command == "I":
            if not heap_dict[value]:
                heapq.heappush(heap_min, value)
                heapq.heappush(heap_max, -value)
            heap_dict[value] += 1
        elif command == "D":
            if value == -1:
                clear(heap_min)
                if not heap_min:
                    continue
                heap_dict[heap_min[0]] -= 1
                if not heap_dict[heap_min[0]]:
                    heapq.heappop(heap_min)
            elif value == 1:
                clear(heap_max, -1)
                if not heap_max:
                    continue
                heap_dict[-heap_max[0]] -= 1
                if not heap_dict[-heap_max[0]]:
                    heapq.heappop(heap_max)

    clear(heap_min)
    clear(heap_max, -1)

    if heap_min and heap_max:
        print(-heap_max[0], heap_min[0])
    else:
        print("EMPTY")
