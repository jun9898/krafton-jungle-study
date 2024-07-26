import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0

# 뿌요
def puyo(puyo_arr):
    for node in puyo_arr:
        graph[node[0]][node[1]] = "."

def puyo_puyo():
    for x in range(6):
        for y in range(10, -1, -1):
            for k in range(11, y, -1):
                if graph[y][x] != "." and graph[k][x] == ".":
                    graph[k][x] = graph[y][x]
                    graph[y][x] = "."

# 생각해보니깐 백트레킹을 쓸 이유가 있나?
# def dfs(y, x, count, color):
#     global result
#     if count == 4:
#         result += 1
#         puyo(y, x)
#         return
#     # 밑에는 dfs 로직
#     for i in range(4):
#         new_y, new_x = y + dy[i], x + dx[i]
#         # 범위 안에 있고 같은 컬러면
#         if 0 <= new_y < 12 and 0 <= new_x < 6 and graph[new_y][new_x] == color:
#             # 탐색 계속

def bfs(y, x, color):
    queue = deque([(y, x)])
    puyo_arr = [(y, x)]
    visited = set()
    visited.add((y, x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            # 범위 안에 있고 같은 컬러면
            if (
                0 <= new_y < 12
                and 0 <= new_x < 6
                and (new_y, new_x) not in visited
                and graph[new_y][new_x] != "."
                and graph[new_y][new_x] == color
            ):
                queue.append((new_y, new_x))
                visited.add((new_y, new_x))
                puyo_arr.append((new_y, new_x))

    if len(puyo_arr) >= 4:
        puyo(puyo_arr)
        puyo_puyo()
        return True
    return False




graph = [list(input().rstrip()) for _ in range(12)]

for i in range(12):
    j = 0
    while j < 6:
        if not bfs(i, j, graph[i][j]):
            j += 1
        else:
            result += 1

print(result)