import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = {i: {} for i in range(1, V+1)}

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w


def dijkstra(graph, start):
    dist = {node : float('inf') for node in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if dist[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            tmp_dist = cur_dist + new_dist
            if tmp_dist < dist[new_dest]:
                dist[new_dest] = tmp_dist
                heapq.heappush(queue, [tmp_dist, new_dest])
    return dist


for node, value in dijkstra(graph, K).items():
    if value == float('inf'):
        print("INF")
    else:
        print(value)
