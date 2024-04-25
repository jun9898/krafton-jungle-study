import sys
import math
input = sys.stdin.readline

maximum = -math.inf
minimum = math.inf


def dfs(answer, cur = 0):
    global maximum, minimum
    if cur >= n-1:
        maximum = max (answer, maximum)
        minimum = min (answer, minimum)
        return
    for i in range(4):
        if operands[i] == 0:
            continue
        operands[i] -= 1

        if i == 0:
            dfs(answer + arr[cur + 1], cur + 1)
            operands[i] += 1
        if i == 1:
            dfs(answer - arr[cur + 1], cur + 1)
            operands[i] += 1
        if i == 2:
            dfs(answer * arr[cur + 1], cur + 1)
            operands[i] += 1
        if i == 3:
            dfs(int(answer / arr[cur + 1]), cur + 1)
            operands[i] += 1


# 입력받을 숫자의 갯수
n = int(input())
arr = list(map(int, input().split()))
operands = list(map(int, input().split()))

dfs(arr[0])
print(maximum)
print(minimum)
