import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
board = []

for _ in range(n):
    score = list(map(int, input().split()))
    if score[0] != k:
        board.append(score)
    else:
        myscore = score

count = 1

for i in range(n-1):
    if board[i][1] > myscore[1]:
        count += 1
    elif board[i][1] == myscore[1]:
        if board[i][2] > myscore[2]:
            count += 1

        elif board[i][2] == myscore[2]:
            if board[i][3] > myscore[3]:
                count += 1

print(count)


