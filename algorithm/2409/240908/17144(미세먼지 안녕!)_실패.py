import sys

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
upDy = [0, -1, 0, 1]
upDx = [1, 0, -1, 0]
downDy = [0, 1, 0, -1]
downDx = [1, 0, -1, 0]

'''
고려해야할 사항
미세먼지의 확산은 모두 동시 다발적으로 일어남
bfs로 확산 처리를 하면 될 것 같지만 조건을 따져봐야함

1. 우선 미세먼지의 위치를 저장하는 queue 생성
2. 모든 미세먼지의 위치를 순회하며 어떤 위치에 몇의 값을 설정해줄건지 계산 <- 이 부분이 문제
    graph를 하나의 거대한 queue에 저장 
    popleft를 사용해 cur_graph를 추출
    tmp_graph를 만들어 계산 후 queue에 append
'''

# 주변 빈칸을 체크하고 tmp_graph를 조작
def check_dust(y, x, cur_graph, tmp_graph):
    # 총 몇방향으로 전파 가능한지 check
    tmp = 0
    for i in range(4):
        newY, newX = y + dy[i], x + dx[i]
        if 0 <= newY < r and 0 <= newX < c and cur_graph[newY][newX] != -1:
            tmp_graph[newY][newX] += cur_graph[y][x] // 5
            tmp += cur_graph[y][x] // 5
    # tmp_graph[y][x] = cur_graph[y][x] - tmp 여기서도 문제 발생! 기존 값을 덮어써버려서 정답과 거리가 먼 결과가 나옴
    tmp_graph[y][x] += cur_graph[y][x] - tmp

# 확산 알고리즘을 작성
def dust_bfs():
    global graph
    tmp_graph = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                check_dust(i, j, graph, tmp_graph)
            elif graph[i][j] == -1:
                tmp_graph[i][j] = -1
    # 여기서 문제 발생 공기청정기 위치 초기화 안함
    graph = tmp_graph

# 공기청정기 로직 작성
def air(machine, dy, dx):
    direct = 0
    before = 0
    curY, curX = machine[0], 1
    while True:
        newY = curY + dy[direct]
        newX = curX + dx[direct]
        if curY == machine[0] and curX == 0:
            break
        if newY < 0 or newY >= r or newX < 0 or newX >= c:
            direct += 1
            continue
        graph[curY][curX], before = before, graph[curY][curX]
        curY, curX = newY, newX

r, c, t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

machine_dis = []

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            machine_dis.append([i, j])

machine_dis.sort()

print(machine_dis)

for _ in range(t):
    dust_bfs()
    air(machine_dis[0], upDy, upDx)
    air(machine_dis[1], downDy, downDx)

print(*graph, sep="\n")

result = 0
for i in graph:
    for j in i:
        if j != -1:
            result += j

print(result)



