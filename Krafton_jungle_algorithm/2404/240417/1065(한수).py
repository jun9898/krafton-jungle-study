import sys
input = sys.stdin.readline

n = int(input())

hansu = 0
for i in range(1, n+1):
    if i < 100:
        hansu += 1
    if i>= 100:
        tmp1 = int(str(i)[0]) - int(str(i)[1])
        tmp2 = int(str(i)[1]) - int(str(i)[2])
        if tmp1 == tmp2:
            hansu += 1

print(hansu)
