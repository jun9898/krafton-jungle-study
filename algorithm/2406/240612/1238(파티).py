import sys
import heapq
input = sys.stdin.readline


def bfs(start_node):
    dist = [float('inf')] * (N + 1)
    dist[start_node] = 0
    q = []
    heapq.heappush(q, (0, start_node))
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] >= weight:
            for v, val in graph[node]:
                if weight + val < dist[v]:
                    dist[v] = weight + val
                    heapq.heappush(q, (weight + val, v))
    return dist


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])

root_visited = bfs(X)
root_visited[0] = 0

for i in range(1, N+1):
    if i != X:
        cur_visited = dfs(i)
        root_visited[i] += cur_visited[X]

print(max(root_visited))
