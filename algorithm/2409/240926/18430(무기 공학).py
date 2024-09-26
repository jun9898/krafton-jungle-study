import sys
input = sys.stdin.readline

def calculate_strength(y, x, dy, dx):
    return woods[y][x] * 2 + woods[y+dy][x] + woods[y][x+dx]

def solve(y, x, strength):
    global N, M, answer
    if x == M:
        x, y = 0, y + 1
    if y == N:
        answer = max(answer, strength)
        return

    if (y, x) not in visited:
        directions = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        for dy, dx in directions:
            ny1, nx1 = y + dy, x
            ny2, nx2 = y, x + dx
            if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M:
                if (ny1, nx1) not in visited and (ny2, nx2) not in visited:
                    visited.update([(y, x), (ny1, nx1), (ny2, nx2)])
                    solve(y, x + 1, strength + calculate_strength(y, x, dy, dx))
                    visited.difference_update([(y, x), (ny1, nx1), (ny2, nx2)])

    solve(y, x + 1, strength)

N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]
visited = set()
answer = 0

solve(0, 0, 0)
print(answer)
