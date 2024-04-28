import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    info = list(input().split())
    arr.append((int(info[0]) ,i ,info[1]))

arr.sort()

for i in arr:
    print(i[0], i[2])