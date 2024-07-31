import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

for i in range(n):
    count = 0
    x, m = map(int,input().split())
    listqueue = deque(list(map(int, input().split())))
    idx = deque(list(range(x)))
    count = 0

    while listqueue:
        if listqueue[0] == max(listqueue):
            count += 1
            listqueue.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(count)
        else:
            listqueue.rotate(-1)
            idx.rotate(-1)

#deque 자료구조를 사용한 문자열 돌려버리기~