import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

count = 0

for i in range(n):
    flag1 = False
    for j in range(m):
        if flag1 == False:
            if arr[i][j] == '-':
                count += 1
                flag1 = True
        elif flag1 == True:
            if arr[i][j] == '|':
                flag1 = False

for i in range(m):
    flag2 = False
    for j in range(n):
        if flag2 == False:
            if arr[j][i] == '|':
                count += 1
                flag2 = True
        elif flag2 == True:
            if arr[j][i] == '-':
                flag2 = False
        
print(count)