import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x, visited):
    for i in range(4):
        new_y, new_x = y + dy[i], x + dx[i]
        if (new_y, new_x) in visited:
            return False
    return True

def dfs(visited, total):
    global result
    if total >= result:
        return
    if len(visited) == 15:
        result = min(result, total)
        return
    for y in range(1, n -1):
        for x in range(1, n -1):
            if (y, x) not in visited and check(y, x, visited):
                temp = [(y, x)]
                temp_cost = graph[y][x]
                for k in range(4):
                    new_y, new_x = y + dy[k], x + dx[k]
                    temp.append((new_y, new_x))
                    temp_cost += graph[new_y][new_x]
                dfs(visited + temp, total + temp_cost)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')
dfs([], 0)

print(result)
