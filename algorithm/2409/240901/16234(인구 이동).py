import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 여기서 병합 가능한 국경을 추려서 그 좌표를 담은 2차원 list를 반환한다.
def check(y, x, visited):
    # 단순 bfs로 인접한 국경중 병합이 가능한 국경을 추린다
    check_list = []
    queue = deque([(y, x)])
    visited.add((y, x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if (
                0 <= new_y < N and
                0 <= new_x < N and
                (new_y, new_x) not in visited and
                L <= abs(graph[cur_y][cur_x] - graph[new_y][new_x]) <= R
            ):
                check_list.append((new_y, new_x))
                visited.add((new_y, new_x))
                queue.append((new_y, new_x))
    if check_list:
        # 병합 가능한 결과 리스트에 본인도 포함시킴
        check_list.append((y, x))
        return check_list

# 받은 2차원 list를 바탕으로 merge
def merge(tmp_result):
    while tmp_result:
        merge_list = tmp_result.popleft()
        merge_average = 0
        for tmp in merge_list:
            cur_y, cur_x = tmp
            merge_average += graph[cur_y][cur_x]
        merge_average //= len(merge_list)
        for tmp in merge_list:
            cur_y, cur_x = tmp
            graph[cur_y][cur_x] = merge_average


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 여기서 반복 횟수를 추린다
result = 0
while True:
    visited = set()
    result_arr = deque()
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                tmp = check(i, j, visited)
                if tmp:
                    result_arr.append(tmp)
    # 만약 반복이 끝난 시점에서 check 함수가 모두 빈 배열을 반환하면 break
    if result_arr:
        merge(result_arr)
        # print(*graph, sep="\n")
        result += 1
    else:
        break

print(result)



