import sys
from collections import deque
input = sys.stdin.readline

# cur_lo는 각 현재 위치와 본인이 몇번 움직였는지에 대한 정보를 담고있음 ex) [0,0]
# if cur_lo[0] in visited || cur_lo[0] > 100: 해당 탐색은 정지
# if cur_lo[0] == ladder_snake[0]: cur_lo의 위치를 ladder_snake[1]로 update
# 위 조건에 모두 부합하지 않으면 1~6의 값을 더해가며 move_queue에 append
# 추가로 이동한 값을 += 1

def bfs(cur_lo):
    move_queue = deque([cur_lo])
    visited = set()
    visited.add(cur_lo[0])
    while move_queue:
        cur_lo = move_queue.popleft()
        if cur_lo[0] == 100:
            return cur_lo
        for i in range(1, 7):
            new_start = cur_lo[0] + i
            if new_start not in visited and new_start <= 100:
                if new_start in ladder_snake:
                    visited.add(new_start)
                    new_start = ladder_snake[new_start]
                if new_start not in visited:
                    visited.add(new_start)
                    move_queue.append([new_start, cur_lo[1] + 1])


n, m = map(int, input().split())

ladder_snake = dict()

for i in range(n + m):
    x, y = map(int, input().split())
    ladder_snake[x] = y

print(bfs([1, 0])[1])

