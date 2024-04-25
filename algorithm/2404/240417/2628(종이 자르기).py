import sys
input = sys.stdin.readline

x, y = map(int, input().split())

dx = [0, x]
dy = [0, y]

n = int(input())

for i in range(n):
    sub_direction, sub = map(int, input().split())
    if sub_direction == 0:
        dy.append(sub)
    elif sub_direction == 1:
        dx.append(sub)

dx.sort()
dy.sort()

res_x, res_y = 0, 0
for i in range(len(dx)-1):
    res_x = max(res_x, dx[i+1]-dx[i])

for i in range(len(dy)-1):
    res_y = max(res_y, dy[i+1]-dy[i])

print(res_x * res_y)


