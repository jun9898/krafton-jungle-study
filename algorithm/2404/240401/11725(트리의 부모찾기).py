import sys
from collections import deque
input = sys.stdin.readline

result = []


def bfs(visited, result):
    queue = deque([1])
    visited.add(1)
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                result[neighbor] = vertex
                visited.add(neighbor)
    return result


n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    vertex, edge = map(int,input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)

result = [0] * (n+1)

result = bfs(set(), result)
for i in range(2, len(result)):
    print(result[i])


