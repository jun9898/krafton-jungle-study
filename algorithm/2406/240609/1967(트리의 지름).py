import sys
sys.setrecursionlimit(10**9)

def dfs(start, current):
    for node, weight in graph[start]:
        if visited[node] == -1:
            visited[node] = current + weight
            dfs(node, visited[node])


n = int(input())
graph = [list([]) for _ in range(n)]
for i in range(n-1):
    V, D, W = map(int, input().split())
    graph[V-1].append([D-1, W])
    graph[D-1].append([V-1, W])

visited = [-1] * n
visited[0] = 0
dfs(0, 0)

start = visited.index(max(visited))
visited = [-1] * n
visited[start] = 0
dfs(start, 0)
print(max(visited))
