import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

result = 0

def make_graph(n):
    global result
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        if plate[v1] == 1 and plate[v2] == 1:
            result += 2
    return graph


# 실외에서 부터 탐색 시작
def find_path(graph, start, res, visited):
    visited.add(start)
    for i in graph[start]:
        if i in visited:
            continue
        if plate[i] == 0:
            find_path(graph, i, res, visited)
        elif plate[i] == 1:
            res.add(i)
    return res


n = int(input())
a = input().rstrip()
plate = [0] * (n+1)
for i in range(1, len(a)+1):
    plate[i] = int(a[i-1])

graph = make_graph(n)

visited = set()
for i in range(1, n+1):
    # 방문한 적 없고, 실외면
    if i not in visited and plate[i] != 1:
        path = (len(find_path(graph, i, set(), visited)))
        result += path * (path - 1)

print(result)
