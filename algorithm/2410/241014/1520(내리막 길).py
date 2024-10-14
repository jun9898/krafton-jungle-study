import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


result = 0

def dfs(y, x):
    global result
    if (y, x) == (n-1, m-1):
        return 1
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            new_y, new_x = y + dy[i], x + dx[i]
            if (
                0 <= new_y < n and
                0 <= new_x < m and
                graph[new_y][new_x] < graph[y][x]
            ):
                dp[y][x] += dfs(new_y, new_x)
    return dp[y][x]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0, 0))

