import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

start_row, start_col, end_row, end_col = map(int, input().split())
grid = [[0 for _ in range(end_col - start_col + 1)] for _ in range(end_row - start_row + 1)]

remaining_cells = (end_col - start_col + 1) * (end_row - start_row + 1)
current_dir = 1
x, y = 0, 0
counter = 1
steps_in_current_dir = 1
last_number = 1

while remaining_cells > 0:
    for _ in range(2):
        for _ in range(steps_in_current_dir):
            if start_row <= x <= end_row and start_col <= y <= end_col:
                grid[x - start_row][y - start_col] = counter
                remaining_cells -= 1
                last_number = counter
            x += dx[current_dir]
            y += dy[current_dir]
            counter += 1
        current_dir = (current_dir - 1) % 4
    steps_in_current_dir += 1

max_length = len(str(last_number))

for row in grid:
    for cell in row:
        print(str(cell).rjust(max_length), end=" ")
    print()
