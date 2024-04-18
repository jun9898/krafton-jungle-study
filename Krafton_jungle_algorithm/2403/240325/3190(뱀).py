from collections import deque

# 방향 : 우 상 좌 하
direction = deque([[1, 0], [0, 1], [-1, 0], [0, -1]])
# 오른쪽 회전
direction.rotate(-1)
# 왼쪽 회전
direction.rotate(1)

n = int(input())

square = [[0 for _ in range(n)] for _ in range(n)]

apple_count = int(input())
for _ in range(apple_count):
    apple_location = list(map(int, input().split()))
    square[apple_location[1]-1][apple_location[0]-1] = 1

move_list = deque()
move_count = int(input())
for _ in range(move_count):
    change_direction = input().split()
    move_list.append(change_direction)

seconds = 0
snake = deque([[0,0]])
# 게임 시작
while True:
    if len(move_list) != 0 and seconds == int(move_list[0][0]) and move_list[0][1] == "L":
        # 왼쪽 회전
        direction.rotate(1)
        move_list.popleft()
    elif len(move_list) != 0 and seconds == int(move_list[0][0]) and move_list[0][1] == "D":
        # 오른쪽 회전
        direction.rotate(-1)
        move_list.popleft()
    snake.append([snake[-1][0]+direction[0][0], snake[-1][1]+direction[0][1]])
    # 머리가 게임판을 벗어나면
    seconds += 1
    if max(snake[-1]) >= n or min(snake[-1]) < 0:
        break
    # 머리가 몸통에 닿으면
    if snake.count(snake[-1]) != 1:
        break
    if square[snake[-1][0]][snake[-1][1]] != 1:
        snake.popleft()
    if square[snake[-1][0]][snake[-1][1]] == 1:
        square[snake[-1][0]][snake[-1][1]] = 0




print(seconds)


