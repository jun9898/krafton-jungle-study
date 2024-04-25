import sys
input = sys.stdin.readline


n, m = map(int, input().split())

plate = []
for i in range(n):
    row = input().rstrip()
    plate.append(row)

count = 0

# 가로 타일 탐색
for i in range(n):
    flag = False
    for j in range(m):
        if plate[i][j] == "-" and flag == False:
            flag = True
            count += 1
        elif flag == True and plate[i][j] == "|":
            flag = False

for i in range(m):
    flag = False
    for j in range(n):
        if plate[j][i] == "|" and flag == False:
            flag = True
            count += 1
        elif flag == True and plate[j][i] == "-":
            flag = False

print(count)




