import sys
input = sys.stdin.readline

n = int(input())

visit = set()

for i in range(n):
    name, status = input().rstrip().split()
    if status == "enter":
        visit.add(name)
    else:
        visit.remove(name)

result = list(visit)
result.sort(reverse=True)
print(*result, sep="\n")
