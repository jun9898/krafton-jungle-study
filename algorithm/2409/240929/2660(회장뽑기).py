import sys
from collections import deque

input = sys.stdin.readline

def bfs(num, visited, dist):
    queue = deque([num])
    while queue:
        cur = queue.popleft()
        for new in graph[cur]:
            if new not in visited:
                visited.add(new)
                queue.append(new)
                dist[new] = dist[cur] + 1
    return max(dist)

n = int(input())
graph = [[] for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    graph[a].append(b)
    graph[b].append(a)

result = []
score = 51

for i in range(1, n + 1):
    visited = {i}
    dist = [0] * (n + 1)
    bfs_res = bfs(i, visited, dist)
    if score > bfs_res:
        result = [i]
        score = bfs_res
    elif score == bfs_res:
        result.append(i)

print(score, len(result))
print(*result)