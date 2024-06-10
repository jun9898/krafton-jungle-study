import sys
from collections import deque
input = sys.stdin.readline


def dfs(start_node, current_weight):
    for new_node, new_weight in graph[start_node]:
        if not visited[new_node]:
            visited[new_node] = current_weight + new_weight
            dfs(new_node, visited[new_node])


n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n):
    commend = deque([x for x in map(int, input().split()) if x != -1])
    dest = commend.popleft()
    while commend:
        node = commend.popleft()
        weight = commend.popleft()
        graph[dest].append([node, weight])
        graph[node].append([dest, weight])

visited = [False] * (n + 1)
visited[1] = True
dfs(1, 0)
max_weight = visited.index(max(visited))

visited = [False] * (n + 1)
dfs(max_weight, 0)
visited[max_weight] = True
print(max(visited))
