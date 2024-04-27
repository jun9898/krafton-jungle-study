import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    n, m = map(int, input().split())
    arr.append((n,m))

arr.sort()
for i in arr:
    print(*i)
