from itertools import combinations

n, m = map(int, input().split())

arr = map(int, input().split())

result = 0

for i in combinations(arr,3):
    if sum(i) <= m and (m - sum(i)) < m - result:
        result = sum(i)

print(result)