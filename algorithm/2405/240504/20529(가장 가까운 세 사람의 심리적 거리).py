import math
import sys
input = sys.stdin.readline


def unique_chars(a, b):
    tmp = 0
    for i, j in zip(a, b):
        if i != j:
            tmp += 1
    return tmp


def dfs_combinations(mbti, length, current, result):
    if len(current) == length:
        result.append(current[:])
        return

    for i in range(len(mbti)):
        current.append(mbti[i])
        dfs_combinations(mbti[i+1:], length, current, result)
        current.pop()

t = int(input())

for i in range(t):
    n = int(input())
    mbti = list(input().rstrip().split())
    if n > 32:
        print(0)
        continue
    res = 13
    result = []
    dfs_combinations(mbti, 3, [], result)
    for a, b, c in result:
        dis = 0
        dis += unique_chars(a, b)
        dis += unique_chars(b, c)
        dis += unique_chars(a, c)
        res = min(res, dis)
    print(res)


