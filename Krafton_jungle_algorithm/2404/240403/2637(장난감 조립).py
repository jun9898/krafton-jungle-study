import sys
from collections import deque
input = sys.stdin.readline


# 위상정렬 후 정렬된 결과값 반환
def topological_sort():
    result = []
    queue = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for index, value in graph[current]:
            in_degree[index] -= 1
            if in_degree[index] == 0:
                queue.append(index)

    return result


def return_result():
    for i in sorted_arr:
        cur_node = i
        for index, value in graph[cur_node]:
            result[index] += result[cur_node] * value


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

basic_parts = set()

# 진입차수와 그래프 생성
for _ in range(m):
    vertex, edge, cost = map(int, input().split())
    graph[vertex].append((edge, cost))
    in_degree[edge] += 1

# 기본부품 구하기
for i in range(1, n+1):
    if len(graph[i]) == 0:
        basic_parts.add(i)

# 위상정렬된 배열 반환
sorted_arr = topological_sort()

result = [0] * (n+1)
result[sorted_arr[0]] = 1
return_result()

for i in range(1, n+1):
    if i in basic_parts:
        print(i, result[i])






