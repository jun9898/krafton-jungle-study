# 3중포문을 사용해 시간 짱오래걸림
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arrayList = [list(map(int, input().split()))for _ in range(n)]

# k = int(input())

# for _ in range(k):
#     i,j,x,y = map(int,input().split())
#     result = 0
#     for a in range(i-1,x):
#         for b in range(j-1,y):
#             result += arrayList[a][b]
#     print(result)

# 누적합 방식을 사용해서 풀이함 집가서 주석달기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
board2 = [[0]*(m+1)] + [[0]*(m+1) for _ in range(n)]

for y in range(1, n+1):
    for x in range(1, m+1):
        board2[y][x] = board2[y-1][x-1]

for a in range(1, n+1):
    for b in range(1, m+1):
        board2[a][b] = board2[a-1][b] + board2[a][b-1] - board2[a-1][b-1] + board[a-1][b-1]
print(board2)

k = int(input())
for i in range(k):
    i,j,x,y = map(int, input().split())
    print(board2[x][y] - board2[i-1][y] - board2[x][j-1] + board2[i-1][j-1]) 