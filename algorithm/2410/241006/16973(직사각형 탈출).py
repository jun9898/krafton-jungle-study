from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

H, W, Sr, Sc, Fr, Fc = map(int, input().split())

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

walls = [(i, j) for i in range(N) for j in range(M) if maps[i][j] == 1]

def move(r, c):
    queue = deque([(r, c)])
    maps[Sr][Sc] = 2  # 시작점 표시

    while queue:
        nowr, nowc = queue.popleft()

        if (nowr, nowc) == (Fr, Fc):
            return maps[Fr][Fc] - 2  # 시작 위치가 2로 표시되므로 2를 뺌

        for d in range(4):
            nr, nc = nowr + dr[d], nowc + dc[d]

            if nr < 0 or nc < 0 or nr > (N - H) or nc > (M - W) or maps[nr][nc] or not check(nr, nc):
                continue

            queue.append((nr, nc))
            maps[nr][nc] = maps[nowr][nowc] + 1  # 이동 거리 증가

    return -1

def check(startr, startc):
    minr, maxr = startr, startr + H
    minc, maxc = startc, startc + W

    for (r, c) in walls:
        if minr <= r < maxr and minc <= c < maxc:
            return False

    return True

Sr, Sc, Fr, Fc = Sr - 1, Sc - 1, Fr - 1, Fc - 1

print(move(Sr, Sc))
