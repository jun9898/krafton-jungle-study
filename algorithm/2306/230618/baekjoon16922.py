from itertools import combinations_with_replacement

n = int(input())
result = []
numbers = [1,5,10,50]

for i in combinations_with_replacement(range(4), n):
    sum = 0
    for j in i:
        sum += numbers[j]
    result.append(sum)
print(len(set(result)))