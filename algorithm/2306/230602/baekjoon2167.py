# 3중포문을 사용해 시간 짱오래걸림
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arrayList = [list(map(int, input().split()))for _ in range(n)]

k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())
    result = 0
    for a in range(i-1,x):
        for b in range(j-1,y):
            result += arrayList[a][b]
    print(result)


# 누적합을 사용해서 시간복잡도를 낮춰보자
import sys
input = sys.stdin.readline

"""
오늘 문제풀이에 사용될 개념은 누적합으로 내가 입력한 2차원 list 의 가로 세로를 한개씩 늘린 list를 만들어
0,0 부터 내가 입력한 x,y의 까지의 값을 모두 더한 2차원 list를 하나 더 만들것이다.
"""

# m, n값을 입력받고 해당 값을 바탕으로 2차원 list와 누적합 값을 입력해줄 list를 하나 더 만들어준다.
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# 가로와 세로 셀을 한개씩 더 만드는 이유는 입력된 누적합을 바탕으로 계산할때 index 에러를 피하기 위해 셀을 한줄 더 만들어준다.
board2 = [[0]*(m+1)] + [[0]*(m+1) for _ in range(n)]

# 누적합을 저장해줄 list에 누적합이 아닌 일반 값을 넣어준다.
"""
ex) 0 0 0 0 
    0 1 2 4 
    0 8 16 32 
"""
for y in range(1, n+1):
    for x in range(1, m+1):
        board2[y][x] = board2[y-1][x-1]

# 각 셀에 누적합을 입력해준다.
"""
ex) 0 0 0 0
    0 1 3 7
    0 9 27 63
"""
for a in range(1, n+1):
    for b in range(1, m+1):
        # 누적합을 구하는 법은 바로 직전의 x-1 열의 값과 y-1의 값을 더한 뒤 x,y열이 중복되는 값을 빼준다
        """
        ex) 0 0 0 0
            0 1 - +
            0 9 + 63(+원래 본인의 수 32)
            +가 위치한 셀의 값을 더해주고
            -가 위치한 셀의 값을 빼준다
        """
        board2[a][b] = board2[a-1][b] + board2[a][b-1] - board2[a-1][b-1] + board[a-1][b-1]

# 범위를 지정해준다.
k = int(input())
for i in range(k):
    i,j,x,y = map(int, input().split())
    # 누적합을 구했던 방법을 응용해 원하는 값을 구해보자.
    print(board2[x][y] - board2[i-1][y] - board2[x][j-1] + board2[i-1][j-1]) 