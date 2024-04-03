import heapq
import sys
from collections import deque


# 위상정렬 후 정렬된 결과값 반환
def topological_sort():
    pq = []
    for i in range(1, n+1):
        # 진입차수가 없으면
        if in_degree[i] == 0:
            # 즉시 최대힙에 더하기
            heapq.heappush(pq, (-i, i))
    # 최대값부터 최대힙을 pop하며 접근할 거기 때문에 현재값을 정해준다.
    res = n
    while pq:
        current = heapq.heappop(pq)[1]
        result[current] = res
        for i in graph[current]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(pq, (-i, i))
        res -= 1

    return result

n = int(input())
in_degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    row = input().rstrip()
    for j in range(len(row)):
        if row[j] == "1":
            graph[int(j)+1].append(i)
            in_degree[i] += 1

result = [0] * (n+1)

sorted_arr = topological_sort()

if sum(sorted_arr) != 0:
    print(*sorted_arr[1:])
else:
    print(-1)