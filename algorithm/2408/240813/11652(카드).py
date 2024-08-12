import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

card = defaultdict(int)

for i in range(n):
    tmp = int(input())
    card[tmp] += 1

result = sorted(card.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])
