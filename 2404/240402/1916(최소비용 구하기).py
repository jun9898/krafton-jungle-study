import math
import sys
import heapq
input = sys.stdin.readline


def make_graph(vertices, edges):
    # 빈 그래프 생성
    graph = [[] for _ in range(vertices+1)]
    for i in range(edges):
        # 그래프에 값 추가
        start_vertex, arrival_vertex, cost  = map(int, input().split())
        graph[start_vertex].append((cost, arrival_vertex))

    return graph

def dijkstra(graph, start_vertex):
    queue = []
    # 거리를 저장할 리스트 선언
    distances = [math.inf] * (vertices + 1)
    # 최초 시작 거리 = 0
    distances[start_vertex] = 0
    heapq.heappush(queue, (0, start_vertex))

    while queue:
        # 현재 정점과 비용
        cur_cost, cur_vertex = heapq.heappop(queue)
        # 이미 저장되어 있는 거리가 더 작으면
        if distances[cur_vertex] < cur_cost:
            continue
        # graph에 저장되어 있는 주변 노드 탐색
        for node in graph[cur_vertex]:
            # 주변 노드 + 자신의 값을 구하고
            cost = cur_cost + node[0]
            # 그 값이 이미 저장되어 있던 값보다 작으면
            if cost < distances[node[1]]:
                # 값을 변경해줌
                distances[node[1]] = cost
                # 그리고 변경된 값을 queue에 넣어서 탐색을 이어감
                heapq.heappush(queue, (cost, node[1]))
    return distances





# 정점의 수
vertices = int(input())
# 간선의 수
edges = int(input())

graph = make_graph(vertices, edges)

start_vertex, arrival_vertex = map(int, input().split())
print(dijkstra(graph, start_vertex)[arrival_vertex])

