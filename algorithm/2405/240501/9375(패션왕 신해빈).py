import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    item_dict = dict()
    mul = 1
    for _ in range(n):
        item_name, item = input().rstrip().split()
        if item not in item_dict:
            item_dict[item] = 1
        else:
            item_dict[item] += 1
    for count in item_dict.values():
        mul *= count + 1
    print(mul - 1)
