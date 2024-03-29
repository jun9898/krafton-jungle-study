import sys


def prim(graph):
    # 그래프의 정점 수
    V = len(graph)

    # 최소 신장 트리를 저장할 리스트
    mst = []

    # 시작 정점을 0번 정점으로 설정
    key = [sys.maxsize] * V  # 각 정점까지의 가중치를 무한대로 초기화
    parent = [None] * V  # 최소 신장 트리에서 각 정점의 부모를 저장할 리스트
    key[0] = 0  # 시작 정점의 가중치를 0으로 설정

    # 이미 선택된 정점을 저장할 집합
    mstSet = set()

    # 모든 정점을 방문할 때까지 반복
    while len(mstSet) < V:
        # 아직 최소 가중치를 가지는 정점을 선택하지 않은 경우
        # 최소 가중치를 가지는 정점을 선택하여 mstSet에 추가
        min_key = sys.maxsize
        min_vertex = None
        for v in range(V):
            if key[v] < min_key and v not in mstSet:
                min_key = key[v]
                min_vertex = v
        mstSet.add(min_vertex)

        # 선택된 정점과 연결된 정점들을 탐색하여 key와 parent를 업데이트
        for v in range(V):
            if graph[min_vertex][v] and v not in mstSet and graph[min_vertex][v] < key[v]:
                key[v] = graph[min_vertex][v]
                parent[v] = min_vertex

    # 최소 신장 트리의 간선들을 구성
    for i in range(1, V):
        mst.append((parent[i], i, graph[i][parent[i]]))

    return mst


# 예제 그래프 (인접 행렬)
graph = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]

# 프림 알고리즘 실행
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)