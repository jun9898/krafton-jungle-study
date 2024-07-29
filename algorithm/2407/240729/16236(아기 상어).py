import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
# 풀이
'''
물고기의 위치를 set 자료형에 담아둬야 한다.
1. 아기상어 뚜루뚜루루 set 자료형으로 visited 유무 판별 (초기화에 유리)
2. 아기상어 기준 위, 왼 (search 함수 만들기)
    a. 상 좌 하 우? 순서로 탐색하기 (조건에 맞으면 bfs 탐색)
        만약 물고기를 먹었다면 탐색 종료 (visited 자료형 초기화, 상어 위치 재정의), 
        거기다 지금 상어가 물고기 몇마리 먹었는지 판별해서 크기 키우기
3. 만약 상어가 다먹었는데 남아있는 물고기가 남아있다면 엄마 호출

global
    상어의 이동 횟수를 저장할 변수 하나
    물고기의 위치를 저장할 set
    탐색 함수 하나
    상어 크기
local
    얼마나 먹었는지 카운트할 계수
    상어의 위치 -> 계속해서 업데이트 될거임
    상어의 방문을 처리할 set 하나
'''

# 물고기를 먹었는지 못먹었는지 여부 반환
def bfs():
    global sharkEatingCount, sharkSize, result, shark
    visited = set()
    visited.add(shark)
    queue = deque([(shark[0], shark[1], 0)])
    min_dist = float('inf')
    candidates = []
    while queue:
        cur_y, cur_x, dist = queue.popleft()

        if dist > min_dist:
            break

        for i in range(4):
            new_y, new_x = (cur_y+dy[i], cur_x+dx[i])
            if (
                0 <= new_y < n and
                0 <= new_x < n and
                (new_y, new_x) not in visited and
                # 같은 사이즈는 통과는 가능
                graph[new_y][new_x] <= sharkSize
            ):
                # 사이즈가 같으면 통과만
                if graph[new_y][new_x] == 0 or graph[new_y][new_x] == sharkSize:
                    visited.add((new_y, new_x))
                    queue.append((new_y, new_x, dist + 1))
                # 먹을 수 있는 물고기라면
                elif graph[new_y][new_x] < sharkSize:
                    candidates.append((new_y, new_x, dist + 1))
                    min_dist = dist + 1
    if not candidates:
        return False
    new_y, new_x, moveCount = sorted(candidates, key=lambda x: (x[2], x[0], x[1]))[0]
    graph[new_y][new_x] = 0
    fish.remove((new_y, new_x))
    sharkEatingCount += 1
    if sharkEatingCount == sharkSize:
        sharkSize += 1
        sharkEatingCount = 0
    shark = (new_y, new_x)

    result += moveCount
    return True


n = int(input())

sharkSize = 2
sharkEatingCount = 0
result = 0

graph = [list(map(int, input().split())) for _ in range(n)]
fish = set()

# 상어 위치, 물고기 위치 초기화 완
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = (i,j)
            # 위치 정보만 쏙 빼오고 귀찮으니 0으로 초기화해두기
            graph[i][j] = 0
        elif graph[i][j] != 9 and graph[i][j] != 0:
            fish.add((i,j))

# 물고기가 남아있을동안 반복
while fish:
    # 탐색!, 먹을 수 있는 물고기가 없었다면 중지
    if not bfs():
        print(result)
        exit()
print(result)







