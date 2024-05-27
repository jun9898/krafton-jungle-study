import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = set()
    visited.add(n)
    n = str(n)
    n = [n, ""]
    dequeue = deque([n])

    while True:
        current = dequeue.popleft()
        current_num = int(current[0])

        if current_num == m:
            print(current[1])
            break

        # D n의 값을 두배로 바꾼다. 9999보다 큰 값이 나오면 % 10000
        temp_D = (current_num * 2) % 10000
        if temp_D not in visited:
            dequeue.append([str(temp_D).zfill(4), current[1] + "D"])
            visited.add(temp_D)

        # S n에서 1을 뺀 결과, n이 0이라면 9999 저장
        temp_S = int(current[0]) - 1
        if temp_S <= 0:
            temp_S = 9999
        if temp_S not in visited:
            dequeue.append([str(temp_S).zfill(4), current[1] + "S"])
            visited.add(temp_S)

        current_deque_L = deque(list(current[0]))
        current_deque_R = deque(list(current[0]))

        # L rotate L
        current_deque_L.rotate(-1)
        current_str_L = ''.join(current_deque_L)
        if int(current_str_L) not in visited:
            dequeue.append([current_str_L.zfill(4), current[1] + "L"])
            visited.add(int(current_str_L))

        # R rotate R
        current_deque_R.rotate(1)
        current_str_R = ''.join(current_deque_R)
        if int(current_str_R) not in visited:
            dequeue.append([current_str_R.zfill(4), current[1] + "R"])
            visited.add(int(current_str_R))







