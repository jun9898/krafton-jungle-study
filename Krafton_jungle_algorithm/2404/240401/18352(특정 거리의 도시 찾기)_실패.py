import sys
import math
input = sys.stdin.readline


def get_smallest():
    min_val = math.inf
    index = 0
    for i in range(1, vertices+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index


def dijkstra(start_vertex):
    distance[start_vertex] = 0
    visited[start_vertex] = True

    # 간선치 초기화
    for i in graph[start_vertex]:
        vertex, weight = i[0], i[1]
        distance[vertex] = weight

    for _ in range(vertices-1):
        now = get_smallest()
        visited[now] = True

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]


vertices, edges, target, start_vertex = map(int, input().split())

visited = [False] * (vertices+1)
distance = [math.inf] * (vertices+1)

graph = [[] for _ in range(vertices+1)]
for _ in range(edges):
    vertex1, vertex2 = map(int, input().split())
    # 연결된 정점과 cost를 등록
    graph[vertex1].append((vertex2, 1))

dijkstra(start_vertex)
if target in distance:
    for i in distance:
        if i == target:
            print(i)
else:
    print(-1)