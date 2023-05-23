import sys
input = sys.stdin.readline
# 재쉬함수의 깊이를 더해주는 기능이다.
sys.setrecursionlimit(10 ** 6)
# 해당 node가 몇번째로 탐색 되었는지 카운트 하기 위한 변수를 할당해준다.
cnt = 1

# DSF 탐색을 시작한다.
def dsf(graph, visited, v):
    # 함수 바깥에 있는 cnt 값을 가져온다.
    global cnt
    # visited에 해당 node가(v) 몇번째로 탐색되었는지 저장한다.
    visited[v] = cnt

    # 해당 node가 어떤 node와 연결되는지 입력되어 있는 graph(v) list를 가져와서 for문을 돌려준다.
    for i in graph[v]:
        # 만약 해당 노드가 카운트 되어있지 않다면
        if visited[i] == 0:
            # count 값을 1 더해주고
            cnt += 1
            # 다음 노트를 탐색한다.
            dsf(graph, visited, i)

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
dsf(graph, visited, r)

# index 0을 제외한 모든 visited 값을 출력해준다.
for i in range(n+1):
    if i != 0:
        print(visited[i])