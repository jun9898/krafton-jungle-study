import sys
from itertools import combinations
input = sys.stdin.readline


def dfs(tmp_graph, value, max_value):
    if not tmp_graph:
        return max(max_value, value)
    for i in tmp_graph:
        max_value = dfs(graph[i[0]], value + i[1], max_value)
    return max_value


def traversal_tree(graph):
    result = 0
    for i in range(len(graph)):
        test = combinations(graph[i], 2)
        for j in test:
            tmp = 0
            for k in j:
                tmp += dfs([k], 0, 0)
            result = max(result, tmp)
    return result


n = int(input())
graph = [list([]) for _ in range(n)]
for i in range(n-1):
    V, D, W = map(int, input().split())
    graph[V-1].append([D-1, W])
    graph[D-1].append([V-1, W])

print(traversal_tree(graph))

