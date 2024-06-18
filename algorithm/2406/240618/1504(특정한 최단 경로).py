import sys
import heapq
input = sys.stdin.readline


def dijkstra(start_node):
    dist = [float('inf')] * (n + 1)
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


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    tmp1, tmp2, weight = map(int, input().split())
    graph[tmp1].append([tmp2, weight])
    graph[tmp2].append([tmp1, weight])

pin1, pin2 = map(int, input().split())

root_dist = dijkstra(1)
pin1_dist = dijkstra(pin1)
pin2_dist = dijkstra(pin2)

version1 = root_dist[pin1] + pin1_dist[pin2] + pin2_dist[n]
version2 = root_dist[pin2] + pin2_dist[pin1] + pin1_dist[n]

result = min(version1, version2)

if result < float('inf'):
    print(result)
else:
    print(-1)

