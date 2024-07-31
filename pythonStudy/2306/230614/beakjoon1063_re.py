king,rock, t = input().split()
t = int(t)
move = [input() for _ in range(t)]


king_x = int(ord(king[0])) - int(ord('A')) + 1
king_y = int(king[1])

rock_x = int(ord(rock[0])) - int(ord('A')) + 1
rock_y = int(rock[1])


alp = ['A','B','C','D','E','F','G','H']

move_type = ['R','L' ,'B' ,'T' ,'RT' ,'LT' ,'RB' ,'LB']
dx = [+1,-1, 0, 0, +1, -1, +1, -1]
dy = [0, 0, -1, +1, +1, +1, -1, -1]

for i in range(t):
    index = move_type.index(move[i])

    if king_x + dx[index] >= 1 and king_x + dx[index] <= 8 and king_y + dy[index] >= 1 and king_y + dy[index] <= 8:
        if king_x + dx[index] == rock_x and king_y + dy[index] == rock_y:
            if rock_x + dx[index] >= 1 and rock_x + dx[index] <= 8 and rock_y + dy[index] >= 1 and rock_y + dy[index] <= 8:
                king_x += dx[index]
                king_y += dy[index]
                rock_x += dx[index]
                rock_y += dy[index]
            else:
                continue
        else:
            king_x += dx[index]
            king_y += dy[index]
    else:
        continue

print(alp[king_x-1]+str(king_y))
print(alp[rock_x-1]+str(rock_y))

