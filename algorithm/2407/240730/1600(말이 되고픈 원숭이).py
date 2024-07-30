import sys
from collections import deque

input = sys.stdin.readline

'''
평범한 BFS에서 약간의 응용이 들어감
horse의 움직임과 monkey의 움직임을 저장
함수에 들어가기 전 0으로 초기화된 그래프 생성
visited, queue 초기화 
    여기서 queue에 들어갈 인자는 x,y 뿐만 아니라 말처럼 움직일 수 있는 횟수, 지금까지 움직인 횟수까지
    curY, curX, horseCount, curMove  = queue에 들어있는 값을 빼온다
    만약 horseCount가 유효하면 > 0
        horse 이동방식으로 graph에 족적 남기고 queue에 위치 더하기 - 함수로 빼놓으면 가독성 올라갈듯
        horseCount -= 1
    아니면
        원숭

탐색이 끝나면 graph[h-1][w-1] 출력
        
global
    원숭, 말 이동 패턴
    0으로 초기화된 graph
    입력받은 graph
local
    각 queue에 들어갈 인자들
    방문을 처리할 set 하나

문제발생!
말을 아껴놨다가 장애물을 넘어갈 수 있는 위치에서만 사용할 수 있게 구현해야함
한차원 높혀서 모든 경우의 수를 판단해야할듯
visited에 horseCount를 포함해 원숭이 -> 말 -> 원숭이 이런 연산도 가능하게 바꿔야함
'''
horseDY = [-2, -1, -2, -1, 2, 1, 2, 1]
horseDX = [-1, -2, 1, 2, -1, -2, 1, 2]

monkeyDY = [-1, 1, 0, 0]
monkeyDX = [0, 0, -1, 1]

K = int(input())

W, H = map(int, input().split())


def likeMonkey(y, x, horseCount, queue, visited, moves):
    for i in range(4):
        newY, newX = y + monkeyDY[i], x + monkeyDX[i]
        if 0 <= newY < H and 0 <= newX < W and graph[newY][newX] == 0 and (newY, newX, horseCount) not in visited:
            queue.append((newY, newX, horseCount, moves + 1))
            visited.add((newY, newX, horseCount))



def likeHorse(y, x, horseCount, queue, visited, moves):
    for i in range(8):
        newY, newX = y + horseDY[i], x + horseDX[i]
        if 0 <= newY < H and 0 <= newX < W and graph[newY][newX] == 0 and (newY, newX, horseCount -1) not in visited:
            queue.append((newY, newX, horseCount - 1, moves + 1))
            visited.add((newY, newX, horseCount - 1))


def bfs():
    # 여기서 queue에 들어갈 인자는 x,y 뿐만 아니라 말처럼 움직일 수 있는 횟수, 지금까지 움직인 횟수까지
    queue = deque([(0, 0, K, 0)])
    visited = {(0, 0, K)}
    while queue:
        curY, curX, horseCount, moves = queue.popleft()

        if curY == H - 1 and curX == W - 1:
            return moves

        likeMonkey(curY, curX, horseCount, queue, visited, moves)
        if horseCount > 0:
            likeHorse(curY, curX, horseCount, queue, visited, moves)
    return -1


graph = []

for _ in range(H):
    graph.append(list(map(int, input().split())))

print(bfs())


