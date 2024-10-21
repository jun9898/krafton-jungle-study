import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_node):
    queue = deque([start_node])
    visited = {start_node}
    result = 0
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                result += 1
    return result

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp2].append(tmp1)

MAX = 0
result = []

for i in range(1, n + 1):
    tmp = bfs(i)
    if tmp > MAX:
        MAX = tmp
        result = [i]
    elif tmp == MAX:
        result.append(i)

print(*result)


