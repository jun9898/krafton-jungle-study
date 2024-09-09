import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        cur, dept = queue.popleft()
        if cur == target:
            return dept
        for i in graph[cur]:
            if i not in visited:
                visited.add(i)
                queue.append((i, dept + 1))



n = int(input())
graph = [[] for _ in range(n+1)]
start, target = map(int, input().split())
m = int(input())
for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

result = bfs()
if result:
    print(result)
else:
    print(-1)