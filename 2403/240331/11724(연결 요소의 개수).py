import sys
sys.setrecursionlimit(1000000)
from collections import deque

input = sys.stdin.readline


def search_connected(res):
    total_visited_vertex[0] = 1
    while sum(total_visited_vertex)-1 != vertex:
        # 방문처리 되지 않은 노드로부터 탐색 시작
        start = total_visited_vertex.index(0)
        dfs(start, set())
        res += 1
    return res


def dfs(start, visited):
    total_visited_vertex[start] = 1
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            dfs(i, visited)
    return


vertex, edge = map(int, input().split())

graph = deque([] for _ in range(vertex + 1))
total_visited_vertex = [0] * (vertex + 1)
res = 0

# 그래프 생성
for i in range(edge):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

print(search_connected(graph, res))

