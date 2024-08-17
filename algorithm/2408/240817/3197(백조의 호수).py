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

해결!!
만약 백조 1의 탐색 영역과 백조 2의 탐색 영역을 set으로 설정해놓고
교집합이 발생했을때 return True로 처리하면 탐색시간을 단축할 수 있을듯 함
'''

def melt():
    global water
    waterCopy = list(water)
    tmpWater = []
    for i in waterCopy:
        curY, curX = i
        for j in range(4):
            newY, newX = curY + dy[j], curX + dx[j]
            # 범위 안에 있고 주변에 얼음이 있다면 가장자리라는 뜻
            if 0 <= newY < r and 0 <= newX < c and graph[newY][newX] == "X":
                # 녹일 얼음 리스트에 추가
                (tmpWater.append((newY, newX)))
    # 모든 가장자리 얼음 탐색이 끝나면 녹이기
    for i in tmpWater:
        meltY, meltX = i
        graph[meltY][meltX] = "."
    # 다음 탐색을 위해 set 초기화
    water = set(tmpWater)


def bfs(visited):
    global swan
    queue = deque(swan)
    tmpSwan = []
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
                if graph[newY][newX] == "X":
                    tmpSwan.append((newY, newX))
                    visited.add((newY, newX))
                else:
                    queue.append((newY, newX))
                    visited.add((newY, newX))
    # 탐색 실패 ㅠㅠ
    swan = deque(tmpSwan)
    return False


def find():
    result = 0
    visited = {(swan[0][0], swan[0][1])}
    while True:
        if bfs(visited):
            return result
        melt()
        result += 1


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

water = set()
swan = list()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            # 백조 위치는 하나만 있어도 됨으로 초기화해도 상관 X
            swan = [(i, j)]
        if graph[i][j] == '.' or graph[i][j] == 'L':
            water.add((i, j))

graph[swan[0][0]][swan[0][1]] = "."
print(find())


