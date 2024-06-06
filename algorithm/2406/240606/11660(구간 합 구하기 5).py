import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] += arr[i-1][0]
    arr[0][i] += arr[0][i-1]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

commend = [list(map(int, input().split())) for _ in range(m)]
commend = [[x1-1, x2-1, x3-1, x4-1] for x1, x2, x3, x4 in commend]

for i in commend:
    x1, x2, x3, x4 = i
    result = arr[x3][x4]
    if x1 > 0:
        result -= arr[x1-1][x4]
    if x2 > 0:
        result -= arr[x3][x2-1]
    if x1 > 0 and x2 > 0:
        result += arr[x1-1][x2-1]
    print(result)
