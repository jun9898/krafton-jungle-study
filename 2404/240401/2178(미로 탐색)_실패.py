import sys
import math
input = sys.stdin.readline


def dfs(plate, x, y, max_y, max_x, res, visited):
    if x < 0 or x > max_x or y < 0 or y > max_y or (x,y) in visited or plate[y][x] == "0":
        return
    if x == max_x and y == max_y:
        res = min(result, res)
        return res
    visited.add((x,y))
    for i in range(4):
        res = dfs(plate, x + dx[i], y + dy[i], max_y, max_x, res, visited)
    return res


n, m = map(int, input().split())
# 동서남북
dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = math.inf

plate = list()
for i in range(n):
    plate.append(list(input().rstrip()))

res = 0
print(dfs(plate, 0, 0, n-1, m-1, res, set()))


