import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

max_value = 0


def dfs(y, x, _sum, count):
    global max_value
    _sum += graph[y][x]
    if count == 4:
        max_value = max(max_value, _sum)
        return
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if 0 <= new_y < n and 0 <= new_x < m and (new_y, new_x) not in visited:
            visited.add((new_y, new_x))
            dfs(new_y, new_x, _sum, count + 1)
            visited.remove((new_y, new_x))


def extra(y, x, _sum, count):
    global max_value
    if count == 4:
        max_value = max(max_value, _sum)
        return
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if 0 <= new_y < n and 0 <= new_x < m and (new_y, new_x) not in visited:
            visited.add((new_y, new_x))
            _sum += graph[new_y][new_x]
            extra(y, x, _sum, count + 1)
            _sum -= graph[new_y][new_x]
            visited.remove((new_y, new_x))



visited = set()
for i in range(n):
    for j in range(m):
        visited.add((i, j))
        dfs(i, j, 0, 1)
        extra(i, j, graph[i][j], 1)
        visited.remove((i, j))

print(max_value)
