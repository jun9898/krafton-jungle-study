import sys
input = sys.stdin.readline

n, m = map(int, input().split())
party = [0] * m
truth = set(map(int, input().split()[1:]))

graph = []

for i in range(m):
    tmp = set(map(int, input().split()[1:]))
    graph.append(tmp)

for _ in range(m):
    for j in graph:
        if j & truth:
            truth = truth.union(j)

result = 0
for i in graph:
    if i & truth:
        continue
    result += 1

print(result)