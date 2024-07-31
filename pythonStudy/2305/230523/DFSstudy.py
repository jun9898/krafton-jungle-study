import sys
input = sys.stdin.readline

def dsf(graph, visited, v):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dsf(graph, visited, i)

n, m, r = map(int, input().split())

graph = [i for i in range(n+1)]

for i in range(m):
    graph.append(list(map(int, input().split())))

visited = [False] * m

dsf(graph, visited, r)