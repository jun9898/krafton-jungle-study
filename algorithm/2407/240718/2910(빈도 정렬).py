import sys
from collections import defaultdict
input = sys.stdin.readline

m, c = map(int, input().split())

d = defaultdict(int)

arr = list(map(int, input().split()))

for i in arr:
    d[i] += 1

for i in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(f"{i[0]} " * i[1], end="")

