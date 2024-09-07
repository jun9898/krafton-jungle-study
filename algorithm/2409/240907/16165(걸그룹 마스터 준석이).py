import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

group_dict = defaultdict(list)
member_dict = defaultdict(list)
for i in range(n):
    group_name = input().rstrip()
    for j in range(int(input())):
        member_name = input().rstrip()
        group_dict[group_name].append(member_name)
        member_dict[member_name].append(group_name)

for i in range(m):
    name = input().rstrip()
    tmp = int(input())
    if tmp == 1:
        print(*member_dict[name])
    elif tmp == 0:
        print(*sorted(group_dict[name]), sep="\n")

