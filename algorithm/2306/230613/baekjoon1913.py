import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list([0]*n)for _ in range(n)]

x = (n-1)//2
y = (n-1)//2
arr[x][y] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

start = 3
i = 2

while x != 0 or y != 0:
    while i <= start * start:
        if x == y == (n-1)//2:
            count_u, count_d, count_l, count_r = start, start-1, start-1, start-2
            y += dy[0]
            x += dx[0]
            count_u -= 1

        elif count_r > 0:
            y += dy[3]
            x += dx[3]
            count_r -= 1

        elif count_d > 0:
            y += dy[1]
            x += dx[1]
            count_d -= 1

        elif count_l > 0:
            y += dy[2]
            x += dx[2]
            count_l -= 1

        elif count_u > 0:
            y += dy[0]
            x += dx[0]
            count_u -= 1
        
        arr[y][x] = i
        i += 1

    start += 2
    n -= 2

for i in range(len(arr)):
    print(*arr[i])
    if m in arr[i]:
        my = i+1
        mx = arr[i].index(m)+1
print(my, mx)
























# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# i = 2
# start = 3

# while x != 0 or y != 0:
#     while i <= start * start:
#         if x == y == (n-1)//2:
#             cnt_up,cnt_down,cnt_left,cnt_right = start, start - 1, start -1, start - 2
#             x += dx[0]
#             y += dy[0]
#             cnt_up -= 1

#         elif cnt_right > 0:
#             x += dx[3]
#             y += dy[3]
#             cnt_right -= 1

#         elif cnt_down > 0:
#             x += dx[1]
#             y += dy[1]
#             cnt_down -= 1

#         elif cnt_left > 0:
#             x += dx[2]
#             y += dy[2]
#             cnt_left -= 1

#         elif cnt_up > 0:
#             x += dx[0]
#             y += dy[0]
#             cnt_up -= 1
        
#         arr[x][y] = i
#         i += 1
    
#     n -= 2
#     start += 2




