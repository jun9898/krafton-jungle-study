array = [list(map(int,input().split()))for _ in range(4)]
size = max(max(array))
board = list(list([0]*101) for _ in range(101))

for i in array:
    for y in range(i[0],i[2]):
        for x in range(i[1],i[3]):
            board[y][x] = 1

result = 0
for i in board:
    result += sum(i)
print(result)
