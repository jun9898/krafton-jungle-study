import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(start, graph, color):
    q = deque([start])
    color[start] = 1

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                color[neighbor] = -color[node]
                q.append(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True

def is_bipartite(n, graph, color):
    for i in range(1, n+1):
        if color[i] == 0:
            if not bfs(i, graph, color):
                return False
    return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    color = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    print("YES" if is_bipartite(N, graph, color) else "NO")
