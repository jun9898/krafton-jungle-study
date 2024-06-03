import sys
input = sys.stdin.readline

n = int(input())

box = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    box[i][0] += min(box[i - 1][1], box[i - 1][2])
    box[i][1] += min(box[i - 1][0], box[i - 1][2])
    box[i][2] += min(box[i - 1][0], box[i - 1][1])
print(min(box[-1]))
