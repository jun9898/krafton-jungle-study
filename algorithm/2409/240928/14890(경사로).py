import sys
input = sys.stdin.readline

def is_valid_slope(road, start, length, check_value, visited):
    for i in range(start, start + length):
        if i >= len(road) or i < 0 or visited[i] or road[i] != check_value:
            return False
        visited[i] = True
    return True

def check_route(road):
    visited = [False] * n  # 경사로가 설치된 곳을 기록할 리스트
    for i in range(n - 1):
        height_diff = road[i] - road[i + 1]  # 현재 위치와 다음 위치의 높이 차

        if height_diff == 0:  # 높이가 같으면 그대로 진행
            continue
        elif abs(height_diff) > 1:  # 높이 차이가 1 이상이면 경사로 설치 불가
            return False
        elif height_diff == 1:  # 내리막길
            if not is_valid_slope(road, i + 1, l, road[i + 1], visited):  # 경사로 설치
                return False
        elif height_diff == -1:  # 오르막길
            if not is_valid_slope(road, i - l + 1, l, road[i], visited):  # 경사로 설치
                return False
    return True

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
for row in arr:  # 가로 길 확인
    if check_route(row):
        result += 1

for col in range(n):  # 세로 길 확인
    if check_route([arr[row][col] for row in range(n)]):
        result += 1

print(result)
