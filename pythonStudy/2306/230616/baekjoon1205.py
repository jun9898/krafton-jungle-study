import sys
input = sys.stdin.readline

n, score, p = map(int,input().split())

cnt = 1
answer = 1

arr = list(map(int,input().split()))

for i in range(n):
    if arr[i] < score:
        break
    elif arr[i] == score:
        cnt += 1
    else:
        answer += 1
        cnt += 1

if cnt > p:
    print(-1)
else:
    print(answer)



