n = int(input())
visit =[[0]*n for _ in range(n)]
arr = [list(map(int,input().split())) for _ in range(n)]

me = [[0,0]] 

dx = (1,0)
dy = (0,1)

while me:
    x, y = me[0][0], me[0][1]
    del me[0]

    if arr[x][y] == -1:
        print("HaruHaru")
        quit()
    
    jump = arr[x][y]

    for i in range(2):
        nx = x + dx[i] * jump
        ny = y + dy[i] * jump

        if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            me.append([nx,ny])

print("Hing")
