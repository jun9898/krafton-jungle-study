import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

in_degree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topological_sort():
    result = []
    queue = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for i in graph[current_node]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=" ")


topological_sort()

