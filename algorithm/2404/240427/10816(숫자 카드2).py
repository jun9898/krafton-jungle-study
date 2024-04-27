import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card_dict = dict()

for i in card:
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

m = int(input())
res = list(map(int, input().split()))
for i in res:
    if i not in card_dict:
        print(0, end=" ")
        continue
    print(card_dict[i], end=" ")