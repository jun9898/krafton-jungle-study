import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    member = list()
    res = 0
    for _ in range(n):
        member.append(list(map(int, input().split())))
    member.sort(key=lambda x: x[0])
    x = member[0][1]
    for i in member:
        if i[1] > x:
            continue
        else:
            x = i[1]
            res += 1
    print(res)



