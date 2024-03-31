import sys
input = sys.stdin.readline

# 크루스칼 알고리즘을 이용한 풀이
v, e = map(int, input().split())
edges = [[int(x) for x in input().split()] for _ in range(e)]
edges.sort(key=lambda x: x[2])  # weight 기준으로 정렬

# 부모를 저장할 테이블
parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i] = i
result = 0


# 재귀적으로 탐색하며 부모를 return
def find_parent(parent, n):
    if n != parent[n]:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]


# 만약 서로의 부모가 겹치지 않으면 parent에 추가
def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 정렬된 배열 기준으로 탐색 시작
for edge in edges:
    x, y, weight = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += weight

print(result)

