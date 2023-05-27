import sys
input = sys.stdin.readline

def chickinDistens(n, m):
    for i in range(n):
        downTownMap = []
        downTownMap.append(input().split() for _ in range(i))
        for j in range(n):
            if downTownMap[i][j] == 1
