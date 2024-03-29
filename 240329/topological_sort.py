def topological_sort(graph):
    # 모든 노드의 진입차수 계산
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # 위상 정렬을 위한 큐 초기화
    queue = [node for node in graph if indegree[node] == 0]

    # 위상 정렬 결과를 담을 리스트
    result = []

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 꺼내 결과 리스트에 추가
        node = queue.pop(0)
        result.append(node)

        # 현재 노드와 연결된 모든 노드의 진입차수를 감소
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            # 진입차수가 0이 되면 큐에 추가
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # 사이클이 존재하는지 여부 검사
    if len(result) != len(graph):
        raise ValueError("그래프에는 사이클이 존재합니다.")

    return result


# 예제 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# 위상 정렬 실행 및 결과 출력
try:
    print("위상 정렬 결과:", topological_sort(graph))
except ValueError as e:
    print("사이클이 존재하여 위상 정렬이 불가능합니다:", e)
