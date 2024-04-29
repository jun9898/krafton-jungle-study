import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_name = set()

for i in range(n):
    name = input().rstrip()
    set_name.add(name)

res = []
count = 0
for i in range(m):
    name = input().rstrip()
    if name in set_name:
        count += 1
        res.append(name)

print(count)
res.sort()
for i in res:
    print(i)


