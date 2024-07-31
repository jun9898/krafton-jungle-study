# import sys
# input = sys.stdin.readline

# m,n = map(int,input().split())
# k = int(input())
# if k > m*n: # 배열의 범위를 벗어남
#     print(0)
#     sys.exit()
    
# board = [[0]*m for _ in range(n)]
# board[0][0] = 1
# move = [(1,0),(0,1),(-1,0),(0,-1)]
# cur_dir = 0
# x,y = (0,0)
# for i in range(2,k+1):
#     while True:
#         a,b = move[cur_dir]
#         dx = x+a; dy = y+b
#         if n>dx>=0 and m>dy>=0 and board[dx][dy] == 0:
#             board[dx][dy] = i
#             x=dx; y=dy # 현재 위치 갱신
#             break
#         else:
#             cur_dir = (cur_dir+1)%4 # 방향전환
# print(y+1,x+1)

"""
아직도 백터를 응용해야하는 시뮬레이션 문제에 확실히 약한것같다.
좀 더 빨리 숙련되야겠다
"""

import sys
input = sys.stdin.readline

m,n = map(int, input().split())
k = int(input())

if k > m*n:
    print(0)
    quit()

board = [list([0]*m)for _ in range(n)]
board[0][0] = 1
move = [(1,0),(0,1),(-1,0),(0,-1)]
dirNum = 0
x,y = (0,0)

for i in range(2,k+1):
    while True:
        a,b = move[dirNum]
        dx = x+a; dy = y+b
        if n> dx >= 0 and m > dy >= 0 and board[dx][dy] == 0:
            board[dx][dy] = i
            x = dx; y = dy
            break
        else:
            dirNum = (dirNum + 1) % 4

print(y+1, x+1)

