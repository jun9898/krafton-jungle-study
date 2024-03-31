import sys
from collections import deque

input = sys.stdin.readline


# 양방향 그래프인걸 깜빡해서 오탑이 떴음
def dfs(start, visited = []):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited


def bfs(start, visited=[]):
    visited.append(start)
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()

print(*dfs(v))
print(*bfs(v))
