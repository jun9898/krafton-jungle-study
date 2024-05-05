import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[math.inf] * (n+1) for _ in range(n+1)]

for i in range(n):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1][tmp2] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 0

print(graph)

for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] != math.inf :
            tmp += graph[i][j]
    print(tmp)

print(res)

