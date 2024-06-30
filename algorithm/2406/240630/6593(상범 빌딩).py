import sys
from collections import deque

input =sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(start_z, start_y, start_x):
    queue = deque()
    queue.append((start_z, start_y, start_x, 0))
    visited.add((start_z, start_y, start_x))
    while queue:
        cur_z, cur_y, cur_x, cur_minute = queue.popleft()
        if graph[cur_z][cur_y][cur_x] == "E":
            return cur_minute
        for i in range(6):
            new_z, new_y, new_x = cur_z + dz[i], cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_z < L and 0 <= new_y < R and 0 <= new_x < C and (new_z, new_y, new_x) not in visited and graph[new_z][new_y][new_x] != "#":
                visited.add((new_z, new_y, new_x))
                queue.append((new_z, new_y, new_x, cur_minute + 1))
    return -1


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    graph = []
    # 3차원 배열 생성
    for z in range(L):
        tmp = []
        for y in range(R):
            tmp_input = (list(input().rstrip()))
            if 'S' in tmp_input:
                start = (z, y, tmp_input.index('S'))
            tmp.append(tmp_input)
        input()
        graph.append(tmp)
    visited = set()
    result = (bfs(start[0], start[1], start[2]))
    print(f"Trapped!" if result == -1 else f"Escaped in {result} minute(s).")




