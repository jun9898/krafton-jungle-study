import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

deque = deque()

deque.append((n, 1))
visited = set()
visited.add(n)

while deque:
    cur = deque.popleft()
    if cur[0] == m:
        print(cur[1])
        exit()
    tmp1 = cur[0] * 2
    tmp2 = (cur[0] * 10) + 1
    if tmp1 <= m and tmp1 not in visited:
        deque.append((tmp1, cur[1] + 1))
        visited.add(tmp1)
    if tmp2 <= m and tmp2 not in visited:
        deque.append((tmp2, cur[1] + 1))
        visited.add(tmp2)

print(-1)
