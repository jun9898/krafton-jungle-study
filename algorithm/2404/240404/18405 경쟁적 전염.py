import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

plate = []
virus = []
visited = [[-1] * n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 바이러스
for i in range(n):
    row = list(map(int, input().split()))
    plate.append(row)
    # 바이러스의 종류 수집
    for j in range(n):
        if plate[i][j] != 0:
            # 바이러스의 종류, Y좌표, X좌표 가져오기
            virus.append((i,j,plate[i][j]))

# 바이러스의 크기에 따라서 정렬
virus.sort(key=lambda x : x[2])
virus = deque(virus)

# S초 뒤에 (Y,X 뒤에 존재하는 바이러스 구하기)
S, Y, X = map(int, input().split())

count = 0

while count != S:
    result_queue = deque()
    while virus:
        # 현재 대기열에 있는 오름차순으로 정렬된 바이러스를 추출
        cur_y, cur_x, cur_virus = virus.popleft()
        # 방문처리
        visited[cur_y][cur_x] = 1
        # 4방향 탐색
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            # 만약 바이러스가 범위를 벗어나지 않고, plate가 전염되지 않았다면
            if 0 <= ny < n and 0 <= nx < n and plate[ny][nx] == 0:
                # 전염시키고 대기열에 추가
                plate[ny][nx] = cur_virus
                result_queue.append((ny, nx, cur_virus))
    # 1 사이클이 종료되면
    # 바이러스 사이클 초기화
    virus = result_queue
    count += 1

print(plate[Y-1][X-1])




