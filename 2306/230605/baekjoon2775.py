# 2775
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    k = int(input())
    floar0 = [i for i in range(1,k+1)]
    for j in range(m):
        for z in range(1, k):
            floar0[z] += floar0[z-1]
    print(floar0[-1])

