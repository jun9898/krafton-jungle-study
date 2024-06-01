import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(y, x, count):
    global result
    result = max(result, count)
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if 0 <= new_y < n and 0 <= new_x < m and not graph[new_y][new_x] in visited:
            visited.add(graph[new_y][new_x])
            dfs(new_y, new_x, count + 1)
            visited.remove(graph[new_y][new_x])


n, m = map(int, input().split())

visited = set()
graph = [list(input().rstrip()) for _ in range(n)]
visited.add(graph[0][0])


dfs(0, 0, 1)
print(result)

