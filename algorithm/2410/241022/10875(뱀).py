import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
L = int(input())
N = int(input())
MAX = L * 2 + 1

dir_map = {'L': 1, 'R': -1, 'S': 0}

moves = [input().split() for _ in range(N)]
moves.append((MAX, 'S'))
lines = [
    (-L-1, -L-1, L+1, -L-1, 0),
    (-L-1, L+1, L+1, L+1, 0),
    (-L-1, -L-1, -L-1, L+1, 1),
    (L+1, -L-1, L+1, L+1, 1)
]

def check_crash(x, y, nx, ny, r):
    temp_lines = lines if len(lines) == 4 else lines[1:]
    closest = MAX

    for sx, sy, ex, ey, d in temp_lines:
        if r % 2 == d % 2:
            if x == nx == sx:
                min_y, max_y = min(sy, ey), max(sy, ey)
                if min_y <= ny <= max_y or min(y, ny) <= min_y < max(y, ny):
                    dist = min_y - y if y < ny else y - max_y
                    closest = min(closest, dist)
            elif y == ny == sy:
                min_x, max_x = min(sx, ex), max(sx, ex)
                if min_x <= nx <= max_x or min(x, nx) <= min_x <= max(x, nx):
                    dist = min_x - x if x < nx else x - max_x
                    closest = min(closest, dist)
        else:
            if sx == ex:
                min_x, max_x = min(x, nx), max(x, nx)
                min_y, max_y = min(sy, ey), max(sy, ey)
                if min_x <= sx <= max_x and min_y <= y <= max_y:
                    closest = min(closest, abs(x - sx))
            elif sy == ey:
                min_y, max_y = min(y, ny), max(y, ny)
                min_x, max_x = min(sx, ex), max(sx, ex)
                if min_y <= sy <= max_y and min_x <= x <= max_x:
                    closest = min(closest, abs(y - sy))

    return closest if closest < MAX else 0

def solve():
    t = 0
    x, y, r = 0, 0, 0

    for move, d in moves:
        move = int(move)
        nx, ny = x + dx[r] * move, y + dy[r] * move
        crash_time = check_crash(x, y, nx, ny, r)

        if crash_time:
            t += crash_time
            return t

        t += move
        lines.insert(0, (x, y, nx, ny, r))
        x, y = nx, ny
        r = (r + dir_map[d]) % 4

    return t

print(solve())
