import sys
a = int(input())
b = int(sys.stdin.readline())
s = [[] for i in range(a+1)]
for i in range(b):
    q1,q2 = map(int,sys.stdin.readline().split())
    s[q1].append(q2)
    s[q2].append(q1)
d = []
for i in s[1]:
    d.append(i)
    for j in s[i]:
        if j!=1 and j not in d:
            d.append(j)
d = list(set(d))
print(len(d))
