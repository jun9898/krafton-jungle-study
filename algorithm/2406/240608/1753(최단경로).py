import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = {i: {} for i in range(1, V+1)}

for i in range(E):
    u, v, w = map(int, input().split())
    # 중복된 간선이 있을 경우 더 작은 가중치를 저장
    if v not in graph[u] or graph[u][v] > w:
        graph[u][v] = w


def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))  # heapq는 튜플을 사용하므로 리스트 대신 튜플 사용

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)

        if cur_dist > dist[cur_dest]:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            tmp_dist = cur_dist + new_dist
            if tmp_dist < dist[new_dest]:
                dist[new_dest] = tmp_dist
                heapq.heappush(queue, (tmp_dist, new_dest))  # 리스트 대신 튜플 사용
    return dist


# 출력
distances = dijkstra(graph, K)
for node in range(1, V + 1):
    if distances[node] == float('inf'):
        print("INF")
    else:
        print(distances[node])
