import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

answer = []
for i in range(n):
    count = -1
    flag = False
    result = []
    for j in range(m):
        if arr[i][j] == '.':
            result.append(count)
            if flag == True:
                count += 1
        elif arr[i][j] == 'c':
            count = 0
            result.append(count)
            count += 1
            flag = True
    answer.append(result)
        

for i in answer:
    print(*i)

