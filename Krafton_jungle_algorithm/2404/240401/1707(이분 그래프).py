import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def make_graph(vertex, edges):
    # 총 정점과 총 간선의 개수
    # 그래프 생성
    graph = [[] for _ in range(vertex + 1)]
    # 간선 정보 입력
    for edge in range(edges):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    # 완성된 그래프 반환
    return graph


# 그래프의 시작점, 그래프를 전달
def is_binary_graph(start, visited, graph, group):
    visited[start] = group

    for neighbor in graph[start]:
        if visited[neighbor] == 0:
            result = is_binary_graph(neighbor, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[neighbor] == group:
                return False
    return True


for _ in range(n):
    vertex, edge = map(int, input().split())
    graph = make_graph(vertex, edge)
    visited = [0] * (vertex + 1)
    is_bipartite = True
    for i in range(1, vertex+1):
        if visited[i] == 0:
            result = is_binary_graph(i, visited, graph, 1)
            if not result:
                is_bipartite = False
                break
    print("YES" if is_bipartite else "NO")




