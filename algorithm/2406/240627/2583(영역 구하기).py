import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(y, x, count):
    queue = deque([(y, x)])
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < M and 0 <= new_x < N and arr[new_y][new_x] == False:
                arr[new_y][new_x] = True
                queue.append((new_y, new_x))
                count += 1
    return count


M, N, K = map(int, input().split())

arr = [[False for _ in range(N)] for _ in range(M)]

for i in range(K):
    tmp = list(map(int, input().split()))
    for j in range(tmp[1], tmp[3]):
        for k in range(tmp[0], tmp[2]):
            arr[j][k] = True


result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == False:
            arr[i][j] = True
            result.append(bfs(i, j, 1))
result.sort()
print(len(result))
print(*result)
