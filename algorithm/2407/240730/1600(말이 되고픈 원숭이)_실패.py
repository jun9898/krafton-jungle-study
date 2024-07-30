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
'''
horseDY = [-2, -1, -2, -1, 2, 1, 2, 1]
horseDX = [-1, -2, 1, 2, -1, -2, 1, 2]

monkeyDY = [-1, 1, 0, 0]
monkeyDX = [0, 0, -1, 1]

K = int(input())

W, H = map(int, input().split())


def likeMonkey(y, x, horseCount, queue, visited):
    for i in range(4):
        newY, newX = y + monkeyDY[i], x + monkeyDX[i]
        if 0 <= newY < H and 0 <= newX < W and graph[newY][newX] == 0 and (newY, newX) not in visited:
            queue.append((newY, newX, horseCount))
            visited.add((newY, newX))
            resultGraph[newY][newX] = resultGraph[y][x] + 1



def likeHorse(y, x, horseCount, queue, visited):
    result = False
    for i in range(8):
        newY, newX = y + horseDY[i], x + horseDX[i]
        if 0 <= newY < H and 0 <= newX < W and graph[newY][newX] == 0 and (newY, newX) not in visited:
            queue.append((newY, newX, horseCount - 1))
            visited.add((newY, newX))
            resultGraph[newY][newX] = resultGraph[y][x] + 1
            result = True
    return result


def bfs():
    # 여기서 queue에 들어갈 인자는 x,y 뿐만 아니라 말처럼 움직일 수 있는 횟수, 지금까지 움직인 횟수까지
    queue = deque([(0, 0, K)])
    visited = set()
    visited.add((0, 0))
    while queue:
        curY, curX, horseCount = queue.popleft()
        if horseCount > 0:
            if not likeHorse(curY, curX, horseCount, queue, visited):
                likeMonkey(curY, curX, horseCount, queue, visited)
        else:
            likeMonkey(curY, curX, horseCount, queue, visited)
        # print()
        # print(*resultGraph, sep="\n")


graph = []
resultGraph = [[0 for _ in range(W)] for _ in range(H)]

for _ in range(H):
    graph.append(list(map(int, input().split())))

bfs()

if resultGraph[H - 1][W - 1] == 0:
    print(-1)
else:
    print(resultGraph[H - 1][W - 1])


