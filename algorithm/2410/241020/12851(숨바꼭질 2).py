import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

def bfs():
    queue = deque([n])
    result = 0
    while queue:
        cur = queue.popleft()
        if cur == m:
            result += 1
            continue
        for i in cur + 1, cur - 1, cur * 2:
            if 0 <= i < MAX:
                if visited[i] == -1 or visited[i] >= visited[cur] + 1:
                    visited[i] = visited[cur] + 1
                    queue.append(i)
    return visited[m], result

n, m = map(int, input().split())
visited = [-1] * MAX
visited[n] = 0
print(*bfs(), sep="\n")



