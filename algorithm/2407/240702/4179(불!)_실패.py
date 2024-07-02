import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, fire):
    fireQueue = deque()
    curQueue = deque()
    tmpFireQueue = deque()
    tmpCurQueue = deque()
    visited = set()
    visited.add(start)
    for i in fire:
        fireQueue.append(i)
    curQueue.append(start)
    count = 1

    while True:

        while fireQueue:
            cur_y, cur_x = fireQueue.popleft()
            for i in range(4):
                new_y, new_x = cur_y + dy[i], cur_x + dx[i]
                if 0 <= new_y < h and 0 <= new_x < w and graph[new_y][new_x] != "F" and graph[new_y][new_x] != "#":
                    graph[new_y][new_x] = "F"
                    tmpFireQueue.append((new_y, new_x))

        while curQueue:
            y, x = curQueue.popleft()
            for i in range(4):
                new_cur_y, new_cur_x = y + dy[i], x + dx[i]
                if new_cur_y >= h or new_cur_y < 0 or new_cur_x >= w or new_cur_x < 0:
                    return count
                if 0 <= new_cur_y < h and 0 <= new_cur_x < w and (new_cur_y, new_cur_x) not in visited and graph[new_cur_y][new_cur_x] != "#" and graph[new_cur_y][new_cur_x] != "F":
                    visited.add((new_cur_y, new_cur_x))
                    tmpCurQueue.append((new_cur_y, new_cur_x))


        if tmpCurQueue:
            fireQueue.extend(tmpFireQueue)
            curQueue.extend(tmpCurQueue)
            tmpCurQueue.clear()
            tmpFireQueue.clear()
            count += 1
        else:
            return -1


h, w = map(int, input().split())
fire = []
graph = []
for j in range(h):
    tmp = list(input().rstrip())
    if "J" in tmp:
        start = (j, tmp.index("J"))
    if "F" in tmp:
        for k in range(len(tmp)):
            if tmp[k] == "F":
                fire.append((j, k))
    graph.append(tmp)
result = bfs(start, fire)

if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)
