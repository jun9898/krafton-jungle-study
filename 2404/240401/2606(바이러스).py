import sys
input = sys.stdin.readline


def dfs(x = 1, visited = set(), res = 0):
    visited.add(x)
    for i in graph[x]:
        if i not in visited:
            dfs(i, visited, res)
    return visited


n = int(input())
total_edge = int(input())

graph = list([] for _ in range(n + 1))

for i in range(total_edge):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)

print(len(dfs())-1)
