import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 모든 방향을 탐색. 이 과정에서는 n, m 범위를 벗어나도 무관
def search(y, x):
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if 0 <= new_y < n and 0 <= new_x < m:
            if graph[new_y][new_x] == 0 and (new_y, new_x) not in visited:
                return True
    return False

# 방향, 위치정보를 받아온다
def simulation(y, x, d):
    result = 1
    visited.add((y, x))
    while True:
        if not search(y, x):
            # 방향을 유지한체 1칸 후진
            back_y, back_x = y + dy[(d + 2) % 4], x + dx[(d + 2) % 4]
            # 만약 후진이 가능하면
            if 0 <= back_y < n and 0 <= back_x < m and graph[back_y][back_x] != 1:
                y, x = back_y, back_x  # 후진 위치 업데이트
            else:
                break  # 후진 불가하면 종료
        # 만약 주변 4칸 중 청소할 수 있는 칸이 존재하면
        else:
            # 반시계 방향으로 90도 회전한다 * 4
            for _ in range(4):
                d = (d + 3) % 4
                new_y, new_x = y + dy[d], x + dx[d]
                # 전진 가능한 칸이면
                if graph[new_y][new_x] == 0 and (new_y, new_x) not in visited:
                    visited.add((new_y, new_x))
                    result += 1
                    y, x = new_y, new_x  # 위치 업데이트
                    break
    return result

n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = set()

print(simulation(y, x, d))
