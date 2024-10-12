import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

'''
n^2로 계산?

2초라서 가능할지도

암만봐도 DP의 개념을 섞어야할것같은데

n^3으로 계산이였네

반대로 빈공간부터 탐색하면?

1. bfs 함수 안에서 총 빈칸의 넓이를 구하고
2. 그동안 탐색하며 만났던 벽의 좌표를 저장해둔다
3. 그 벽에 빈칸의 총 넓이를 +=
'''

def bfs(start):
    start_y, start_x = start
    visited.add((start_y, start_x))
    queue = deque([(start_y, start_x)])
    count = 1
    tmp_set = set()
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = (cur_y + dy[i], cur_x + dx[i])
            if 0 <= new_y < n and 0 <= new_x < m and (new_y, new_x) not in visited:
                # 벽 저장
                if graph[new_y][new_x] >= 1 and (new_y, new_x) not in tmp_set:
                    tmp_set.add((new_y, new_x))
                # 빈공간이라면 count
                elif graph[new_y][new_x] == 0:
                    queue.append((new_y, new_x))
                    count += 1
                    visited.add((new_y, new_x))
    for i in tmp_set:
        wall_y, wall_x = i
        graph[wall_y][wall_x] += count


n, m = map(int, input().split())

graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = set()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and (i, j) not in visited:
            bfs((i, j))

for i in graph:
    for j in i:
        if j >= 10:
            # 에휴
            j = j % 10
        print(j, end='')
    print()