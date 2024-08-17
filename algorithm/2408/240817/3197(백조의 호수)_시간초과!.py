import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

'''
빙산 + bfs로 생각하면 될듯 함

모든 빙산의 위치 좌표를 set 자료형에 저장
백조 한마리의 위치정보 담기
day = 0
while True:
    tmpIce = []
    set 자료형을 순회하며 물과 접촉하는 빙산을 탐색
        만약 접촉한다면 set에서 제외하고 tmpIce에 append
    tmpIce에 저장되어있는 ice를 모두 녹임
    백조 bfs 순회 시작
    day += 1
    
시간초과!!
내 생각엔 지금 BFS가 탐색해야할 범위가 너무 넓어서 시간초과가 나는것 같음.
이를 임시큐를 만들어 해결해야할것같음
'''

def melt():
    tmpIce = []
    iceCopy = list(ice)
    for i in iceCopy:
        curY, curX = i
        for j in range(4):
            newY, newX = curY + dy[j], curX + dx[j]
            # 범위 안에 있고 주변에 물이 있다면
            if 0 <= newY < r and 0 <= newX < c and (graph[newY][newX] == "." or graph[newY][newX] == "L"):
                # 녹일 얼음 리스트에 추가
                tmpIce.append((curY, curX))
                break
    # 모든 얼음 탐색이 끝나면 녹일 얼음 리스트에 있는 얼음을 녹이기
    for i in tmpIce:
        meltY, meltX = i
        graph[meltY][meltX] = "."
        ice.remove((meltY, meltX))


def bfs():
    queue = deque([swan])
    visited = {swan}
    while queue:
        curY, curX = queue.popleft()
        # 도착!
        if graph[curY][curX] == 'L' :
            return True
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if (
                0 <= newY < r and
                0 <= newX < c and
                (newY, newX) not in visited
            ):
                visited.add((newY, newX))
                queue.append((newY, newX))
    # 탐색 실패 ㅠㅠ
    return False


def find():
    result = 0
    while True:
        if bfs():
            return result
        melt()
        result += 1


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

ice = set()
swan = tuple()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            # 백조 위치는 하나만 있어도 됨으로 초기화해도 상관 X
            swan = (i, j)
        if graph[i][j] == 'X':
            ice.add((i, j))

graph[swan[0]][swan[1]] = "."
print(find())


