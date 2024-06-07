import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(y, x, count, move_count):
    if count >= 2:
        print(1)
        exit()
    if move_count >= 3:
        return
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if 0 <= new_y < 5 and 0 <= new_x < 5 and arr[new_y][new_x] != -1 and (new_y, new_x) not in visited:
            visited.add((new_y, new_x))
            if arr[new_y][new_x] == 1:
                dfs(new_y, new_x, count + 1, move_count + 1)
            else:
                dfs(new_y, new_x, count, move_count + 1)
            visited.remove((new_y, new_x))


arr = [list(map(int, input().split())) for _ in range(5)]
visited = set()

y, x = map(int, input().split())

visited.add((y, x))
dfs(y, x, 0, 0)
print(0)