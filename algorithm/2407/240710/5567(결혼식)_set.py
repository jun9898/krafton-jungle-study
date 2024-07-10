import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    visited = set()

visited.add(1)

for i in graph[1]:
    visited.add(i)
    for j in graph[i]:
        visited.add(j)
print(len(visited)-1)

