import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(m):
    v1, v2, weight = map(int, input().split())
    arr.append([v1, v2,  weight])
print(arr)
