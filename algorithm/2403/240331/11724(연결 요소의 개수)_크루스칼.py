import sys


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    union_parent(parent, u, v)

conneted = set()
for v in parent:
    conneted.add(find_parent(parent,v))
print(len(conneted)-1)
