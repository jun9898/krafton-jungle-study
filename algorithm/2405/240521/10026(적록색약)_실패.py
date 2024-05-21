import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
diff_count = 0
visited = set()


def bfs(y, x):
    global diff_count
    global count
    if (y, x) in visited:               # 만약 이미 방문한 블럭이라면
        return
    visited.add((y, x))                 # 아니면 visited에 add 하고 deque에도 add
    queue = deque([(y, x)])
    flag = graph[y][x]  # 색의 기준을 정하는 flag 설정
    while queue:                 # 탐색 시작
        cur_y, cur_x = queue.popleft()
        if graph[cur_y][cur_x] != flag:
            diff_count += 1
            flag = graph[cur_y][cur_x]
        visited.add((cur_y, cur_x))
        for j in range(4):              # 상하좌우 탐색 시작
            new_y = cur_y + dy[j]
            new_x = cur_x + dx[j]
            if (new_y < 0 or new_y >= n or  # 범위를 벗어난 경우의수 컷
                new_x < 0 or new_x >= n or
                (new_y, new_x) in visited): continue
            if graph[new_y][new_x] == flag: # 같은 색일땐
                queue.appendleft((new_y, new_x))
            elif ((flag == "R" and graph[new_y][new_x] == "G") or
                  (flag == "G" and graph[new_y][new_x] == "R")):
                queue.append((new_y, new_x))
    count += 1

# 1. flag 색과 다른 색이 나왔는데 만약 적 -> 록, 녹 -> 적 이면
# 2. 해당 색을 모두 탐색하고 def_count += 1
# 고민해야 할 점 : 그럼 탐색 함수를 2개를 작성해야 하는건가? 하나의 함수 내에서 모두 진행할 순 없는건가?

n = int(input())
graph = []

for i in range(n):
    row = list(input().rstrip())
    graph.append(row)

for i in range(n):
    for j in range(n):
        bfs(i, j)

print(count + diff_count, count)


