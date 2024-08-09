import sys
input = sys.stdin.readline

'''
세대만큼 반복
여기서 반복되는 패턴은 
i(기존 방향) + 1 for i in (기존 방향)
i.reverse (뒤집기)
(기존 이동방향) + (1 더하고 뒤집은 루트)
'''

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n = int(input())
graph = [[False] * 101 for _ in range(101)]

def count(i, j):
    if (
        graph[i][j] and
        graph[i][j + 1] and
        graph[i + 1][j] and
        graph[i + 1][j + 1]
    ):
        return True

# 밟아왔던 경로에 + 1 후 뒤집기
def redirection(total_direction, tmp_direction):
    tmp_direction = [(i + 1) % 4 for i in total_direction]
    tmp_direction.reverse()
    return total_direction + tmp_direction, tmp_direction

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[y][x] = True
    # 총 경로를 저장할 배열과 임시 배열(더하고 뒤집기) 초기화
    tmp_direction = [d]
    total_direction = [d]
    # 세대만큼 반복
    for _ in range(g + 1):
        for i in tmp_direction:
            y, x = y + dy[i], x + dx[i]
            if 0 <= y < 101 and 0 <= x < 101:
                graph[y][x] = True
        total_direction, tmp_direction = redirection(total_direction, tmp_direction)

    result = 0
    for i in range(100):
        for j in range(100):
            if count(i, j):
                result += 1

print(result)
