import sys
input = sys.stdin.readline

white = 0
blue = 0

def back_tracking(start_x, start_y, length):
    global white, blue
    result = search(start_x, start_y, length)
    if result == 0:
        white += 1
        return
    if result == 1:
        blue += 1
        return
    mid = length // 2
    back_tracking(start_x, start_y, mid)
    back_tracking(start_x + mid, start_y , mid)
    back_tracking(start_x, start_y + mid, mid)
    back_tracking(start_x + mid, start_y + mid, mid)

def search(start_x, start_y, length):
    flag = arr[start_x][start_y]
    for i in range(start_x, start_x + length):
        for j in range(start_y, start_y + length):
            if arr[i][j] != flag:
                return 2
    return flag


n = int(input())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

back_tracking(0, 0, len(arr))

print(white)
print(blue)
