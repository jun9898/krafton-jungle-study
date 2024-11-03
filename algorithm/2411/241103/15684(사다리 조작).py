import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
grid = [[0] * n for _ in range(h)]

for _ in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1

def check_path():
    for start in range(n):
        curr = start
        for level in range(h):
            if grid[level][curr]:
                curr += 1
            elif curr > 0 and grid[level][curr-1]:
                curr -= 1
        if curr != start:
            return False
    return True

def solve(count, row, col):
    global result
    if result <= count:
        return
    if check_path():
        result = min(result, count)
        return
    if count == 3:
        return
    for i in range(row, h):
        for j in range(n-1):
            if not grid[i][j]:
                grid[i][j] = 1
                solve(count + 1, i, j + 2)
                grid[i][j] = 0

result = 4
solve(0, 0, 0)
print(-1 if result > 3 else result)
