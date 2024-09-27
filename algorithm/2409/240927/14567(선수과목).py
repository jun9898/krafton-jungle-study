import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque([i for i in range(1, N+1) if indegree[i] == 0])
    answer = [1] * (N+1)

    while q:
        now = q.popleft()
        result.append(now)

        for next_node in graph[now]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
            answer[next_node] = max(answer[next_node], answer[now] + 1)

    print(*answer[1:])

topology_sort()