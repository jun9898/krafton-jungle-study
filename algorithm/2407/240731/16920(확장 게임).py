import sys
from collections import deque, defaultdict

input = sys.stdin.readline

'''
우선 bfs 탐색을 할거임
하지만 여기서 while queue가 아닌 S의 숫자만큼 반복 -> index로 판별하면 될듯
2중 queue를 사용하면 될것같음! + key값을 index로 둬도 좋을듯

각 플레이어의 위치를 2차원 queue에 저장 ex) [{i : [(1, 2), (3, 4)]}, {i : [(5,5]}]
    여기서 queue에 있는 queue를 하나 빼오고 이걸로 탐색 시작
    while True가 아닌 for i in range(S[index])
        자잘한 조건 붙여서 확장
    
    반복이 끝나면 queue의 최종 형태를 globalQueue에 append (queue가 비어있으면 pass)

global
    최초 전체 플레이어의 위치를 저장할 queue(dict(queue()))
    graph
local
    key값
    그냥 평범한 bfs에 필요한것들
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while globalQueue:
        curDict = globalQueue.popleft()
        curKey = list(curDict.keys())[0]
        curQueue = curDict[curKey]
        if curQueue:
            for _ in range(S[curKey]):
                tmpQueue = deque()
                while curQueue:
                    curY, curX = curQueue.popleft()
                    for i in range(4):
                        newY, newX = curY + dy[i], curX + dx[i]
                        if 0 <= newY < N and 0 <= newX < M and graph[newY][newX] == ".":
                            graph[newY][newX] = str(curKey)
                            tmpQueue.append((newY, newX))
                curQueue = tmpQueue
            globalQueue.append({curKey:curQueue})


N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))

graph = [list(input().rstrip()) for _ in range(N)]

globalQueue = deque()
positions = defaultdict(deque)

for p in range(1, P+1):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == str(p):
                positions[p].append((i, j))
    globalQueue.append({p : positions[p]})
bfs()

for result in range(1, P+1):
    count = 0
    for i in graph:
        for j in i:
            if j == str(result):
                count += 1
    print(count, end=" ")



