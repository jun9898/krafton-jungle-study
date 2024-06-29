import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end):
    queue = deque()
    queue.append(start)
    arr[start] = 1
    while queue:
        cur = queue.popleft()
        if cur == end:
            return arr[cur] - 1
        for i in range(2):
            new = cur + dx[i]
            if 0 <= new < F:
                if arr[new] == 0:
                    queue.append(new)
                    arr[new] = arr[cur] + 1
    return -1


F, S, G, U, D = map(int, input().split())

arr = [0] * F

dx = [U, -D]

result = bfs(S - 1, G - 1)
if result == -1:
    print("use the stairs")
    exit(0)
print(result)
