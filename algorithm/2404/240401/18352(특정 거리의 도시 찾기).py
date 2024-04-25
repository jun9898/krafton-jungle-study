import sys
import heapq
import math
input = sys.stdin.readline


def dijkstra(start_vertex):
    pq = []
    heapq.heappush(pq, (0, start_vertex))
    distance[start_vertex] = 0

    while pq:
        cur_cost, cur_vertex = heapq.heappop(pq)
        if distance[cur_vertex] < cur_cost:
            continue
        for vertex in graph[cur_vertex]:
            cost = cur_cost + vertex[1]
            if cost < distance[vertex[0]]:
                distance[vertex[0]] = cost
                heapq.heappush(pq, (cost, vertex[0]))


vertices, edges, target, start_vertex = map(int, input().split())

fixed = [False] * (vertices+1)
distance = [math.inf] * (vertices+1)

graph = [[] for _ in range(vertices+1)]

for _ in range(edges):
    vertex1, vertex2 = map(int, input().split())
    # 연결된 정점과 cost를 등록
    graph[vertex1].append((vertex2, 1))


dijkstra(start_vertex)

if target in distance:
    for i in range(1, vertices+1):
        if distance[i] == target:
            print(i)
else:
    print(-1)
