import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        cur = queue.popleft()
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                visited[neighbor] = visited[cur] + 1
                queue.append(neighbor)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
bfs(1)

max_dist = max(visited)
print(visited.index(max_dist), max_dist - 1, visited.count(max_dist))
