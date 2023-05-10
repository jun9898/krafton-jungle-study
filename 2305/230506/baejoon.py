
# table = [input() for i in range(5)]
# for j in range(15):
#     for i in range(5):
#         if j < len(table[i]):
#             print(table[i][j], end='')

table = [([0]*101) for i in range(101)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for r in range(10):
        for c in range(10):
            table[x+r][y+c] = 1

result = 0
for i in table:
    result += sum(i)
print(result)
