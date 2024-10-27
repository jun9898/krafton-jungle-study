import sys
from collections import deque
input = sys.stdin.readline

def bfs(selected):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동
    visited = [[False] * 5 for _ in range(5)]
    queue = deque([selected[0]])
    visited[selected[0][0]][selected[0][1]] = True
    connected_count = 1

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 5 and 0 <= new_col < 5 and not visited[new_row][new_col] and (new_row, new_col) in selected:
                visited[new_row][new_col] = True
                connected_count += 1
                queue.append((new_row, new_col))

    return connected_count == 7  # 모든 여학생이 연결되어 있으면 True 반환

def dfs(depth, start, y_count):
    global result

    if y_count >= 4:
        return

    if depth == 7:
        if bfs(selected):
            result += 1
        return

    for i in range(start, 25):
        row, col = divmod(i, 5)
        selected.append((row, col))
        dfs(depth + 1, i + 1, y_count + (students[row][col] == 'Y'))
        selected.pop()

# 입력 및 초기화
students = [list(input().rstrip()) for _ in range(5)]
selected = []
result = 0

dfs(0, 0, 0)

print(result)
