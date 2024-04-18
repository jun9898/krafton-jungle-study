import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def make_graph(n):
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


# 실내에서 부터 탐색 시작
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

res = 0
visited = set()
for i in range(1, n+1):
    if i not in visited and plate[i] != 0:
        res += len(find_path(graph, i, set(), visited))

print(res)
