import sys
from collections import deque
input = sys.stdin.readline

'''
. 바다
# 암초
* 보물
K 배
'''

fair_winds_y = [1, -1, 0]
fair_winds_x = [1, 1, 1]

contrary_wind_y = [1, 1, -1, -1, 0]
contrary_wind_x = [0, -1, 0, -1, -1]

def check_fairway(new_y, new_x, visited):
    if (
        0 <= new_y < h
        and 0 <= new_x < w
        and (new_y, new_x) not in visited
        and graph[new_y][new_x] != "#"
    ):
        return True



def bfs():
    queue = deque([(start_y, start_x, 0)])
    visited = {(start_y, start_x)}
    while queue:
        cur_y, cur_x, step = queue.popleft()
        if graph[cur_y][cur_x] == "*":
            return step
        # 순풍 계산
        for i in range(3):
            fair_new_y, fair_new_x = cur_y + fair_winds_y[i], cur_x + fair_winds_x[i]
            if check_fairway(fair_new_y, fair_new_x, visited):
                queue.append((fair_new_y, fair_new_x, step))
                visited.add((fair_new_y, fair_new_x))
        # 역풍 계산
        for j in range(5):
            contrary_new_y, contrary_new_x = cur_y + contrary_wind_y[j], cur_x + contrary_wind_x[j]
            if check_fairway(contrary_new_y, contrary_new_x, visited):
                queue.append((contrary_new_y, contrary_new_x, step + 1))
                visited.add((contrary_new_y, contrary_new_x))
    return -1


h, w = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if graph[i][j] == "K":
            start_y, start_x = i, j

print(bfs())