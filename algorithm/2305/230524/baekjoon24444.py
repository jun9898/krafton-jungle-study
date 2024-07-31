import sys
input = sys.stdin.readline
from collections import deque

# 해당 node가 몇번째로 탐색 되었는지 카운트 하기 위한 변수를 할당해준다.
cnt = 1

# BSF 탐색을 시작한다.
def bsf(graph, visited, v):
    # 함수 바깥에 있는 cnt 값을 가져온다.
    global cnt
    # visited에 첫번째  node가(v) 몇번째로 탐색되었는지 저장한다.
    # BSF 탐색은 재귀 함수를 쓰지 않기때문에 첫번째 node를 방문했음을 직접 입력해줘야 한다.
    visited[v] = cnt
    # queue에 시작 node인 v를 넣어준다.
    queue = deque([v])

    # queue에 남은 값이 없을때까지 반복문을 실행해준다.
    while queue:
        # queue에 가장 왼쪽에 있는 값을 pop으로 추출해준다.
        v = queue.popleft()
        # 해당 노드의 연결되어 있는 노드의 값을 i에 넣고 반복해준다.
        for i in graph[v]:
            # 만약 노드 i가 방문처리가 되있지 않다면.
            if visited[i] == 0:
                # queue 에 노드 i를 넣어준다.
                queue.append(i)
                # cnt 1을 해주고
                cnt += 1
                # 해당 노드가 방문된 숫자를 삽입해준다.
                visited[i] = cnt

# 노드의 개수, 노선의 개수, 시작 노드값을 입력받는다.
n, m, r = map(int, input().split())

# graph에 해당 노드가 어떤 노드와 연결되어있는지 저장할 list를 만들어준다
graph = [[]*i for i in range(n+1)]

# 노선의 개수만큼 반복한다
for i in range(m):
    # x값과 y값을 입력받고 해당 노드들끼리 연결되어있음을 표시하기 위해 graph에 서로 교차하여 값을 추가해준다.
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 그렇게 graph에 연결되어있는 노드 입력이 완료되면 값을 정렬해준다.
for i in range(n+1):
    graph[i].sort()

# 노드가 몇번째로 카운트 되었는지 배열을 만들어 저장한다.
visited = [0] * (n+1)

# 탐색 시작
bsf(graph, visited, r)

# index 0을 제외한 모든 visited 값을 출력해준다.
for i in range(n+1):
    if i != 0:
        print(visited[i])