import sys
input = sys.stdin.readline
inf = float('inf')

n = int(input())
m = int(input())

graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start][end] = min(weight, graph[start][end])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print("\n".join(" ".join("0" if graph[row][value] == inf else str(graph[row][value]) for value in range(1, n+1)) for row in range(1, n+1)))


