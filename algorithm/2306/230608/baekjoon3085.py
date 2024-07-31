# 브루트 포스 알고리즘
import sys
input = sys.stdin.readline


def check(board):
    n = len(board)
    result = 1
    for i in range(n):
        score = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                score += 1
            else:
                score = 1
            if score > result:
                result = score
        score = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                score += 1
            else:
                score = 1
            if score > result:
                result = score
    return result

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = check(board)
            if temp > result:
                result = temp
            result = max(check(board), result)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board)
            if temp > result:
                result = temp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(result)

        
