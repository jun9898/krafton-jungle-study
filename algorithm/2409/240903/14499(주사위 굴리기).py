import sys
from collections import deque

input = sys.stdin.readline

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

def turn(dice, dir):
    if dir == 1:   return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif dir == 2: return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif dir == 3: return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:          return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

n, m, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = deque(map(int, input().split()))

dice = [0] * 6

for command in commands:
    ny, nx = y + dy[command-1], x + dx[command-1]

    if 0 <= ny < n and 0 <= nx < m:
        y, x = ny, nx
        dice = turn(dice, command)

        if graph[y][x] == 0:
            graph[y][x] = dice[5]
        else:
            dice[5], graph[y][x] = graph[y][x], 0

        print(dice[0])
