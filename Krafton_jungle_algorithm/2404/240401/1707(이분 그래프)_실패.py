import sys
from collections import deque
input = sys.stdin.readline

n = int(input())


def make_graph(vertex_and_edge):
    # 총 정점과 총 간선의 개수
    total_vertex, total_edge = vertex_and_edge[0], vertex_and_edge[1]
    # 그래프 생성
    graph = [[] for _ in range(total_vertex + 1)]
    rb = [[] for _ in range(total_vertex + 1)]
    # 간선 정보 입력
    for edge in range(total_edge):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    # 완성된 그래프 반환
    return graph, rb


# 그래프의 시작점, 그래프를 전달
def is_binary_tree(graph, rb, visited):
    flag = True
    queue = deque([1])
    rb[1].append(flag)
    while queue:
        root_vertex = queue.popleft()
        visited.add(root_vertex)
        if root_vertex not in visited:
            for neighbor in graph[root_vertex]:
                if flag in rb[neighbor]:
                    return False
                else:
                    flag = not flag
                    rb[neighbor].append(flag)
                    queue.append(neighbor)
    return True



for i in range(n):
    graph, rb = make_graph(list(map(int, input().split())))
    if is_binary_tree(graph, rb, set()):
        print("YES")
    else:
        print("NO")




