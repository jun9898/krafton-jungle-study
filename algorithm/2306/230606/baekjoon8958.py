# 주석 처리하기
import sys
input = sys.stdin.readline

n = int(input())
flag = False

for i in range(n):
    answer = input().rstrip()
    result = 0
    i = 1
    for j in answer:
        if flag == False:
            if j == "O":
                result += i
                flag = True
            else:
                i = 1
                continue
        elif flag == True:
            if j == "O":
                i += 1
                result += i
            else:
                i = 1
                flag = False
    print(result)
    flag = False

        