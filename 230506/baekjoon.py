# score = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0  , 'D+' : 1.5, 'D0' : 1.0, 'F' : 0}

# addScore = 0
# allScore = 0

# for i in range(20):
#     x, y, z = input().split()
#     if z != 'P':
#         addScore += float(y)
#         allScore += float(y) * score[z]
    
# print('%.6f' % (allScore/addScore))

# N ,M = int(input().split())
# for i in range(N):
#     x, y, z = int(input().split())

# n, m = map(int,input().split())
# x = [list(map(int, input().split())) for i in range(n)]
# y = [list(map(int, input().split())) for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         x[i][j] += y[i][j]

# for i in x:
#     print(*i)

maxNum = 0
maxRow, maxCol = 0, 0

table = [list(map(int, input().split())) for i in range(9)]

for y in range(9):
    for x in range(9):
        if maxNum <= table[y][x]:
            maxRow = x+1
            maxCol = y+1
            maxNum = table[y][x]

print(maxNum)
print(maxCol, maxRow)


