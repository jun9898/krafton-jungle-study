import sys

input = sys.stdin.readline

n = int(input())

result = []
for i in range(n):
    a, b = input().split()
    res = ""
    for j in b:
        res += j*int(a)
    result.append(res)

print(*result, sep='\n')