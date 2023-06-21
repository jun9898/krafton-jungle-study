import sys
input = sys.stdin.readline

"""
맵을 입력받는다.
. = 0, X = 1 로 맵을 재구성한다.
모든 배열을 탐색한다
    만약 1을 발견한다면 상 하 좌 우로 탐색 시작한다.
        해당 칸이 0 이라면 count += 1
        count의 값이 3보다 같거나 크다면 그 칸을 1 => 0으로 바꾼다

모든 탐색, 변환과정이 완료된다면 맵을 재구성 한다.
    맵의 가장 윗줄을 더해봤을때 그 값이 0이라면 해당 라인을 del
        값이 1 이상이라면 반복을 중단한다.
    맵의 가장 아럇줄을 더해봤을때 그 값이 0이라면 해당 라인을 del
        값이 1 이상이라면 반복을 중단한다.
    맵의 가장 왼쪽줄을 더해봤을때 그 값이 0이라면 해당 라인을 del
        값이 1 이상이라면 반복을 중단한다.
    맵의 가장 오른쪽줄을 더해봤을때 그 값이 0이라면 해당 라인을 del
        값이 1 이상이라면 반복을 중단한다.

    구현 힘드렁
"""
def search(i,j):
    count = 0
    if plate[i][j] == 1:
        for commend in xy:
            dx = i+commend[0]
            dy = j+commend[1]
            if plate[dx][dy] == 0 :
                count += 1
        if count < 3:
            arr[i][j] = 1


n, m = map(int,input().split())

plate = [list(input().rstrip()) for _ in range(n)]
arr = [list([0]*(m+2)) for _ in range(n+2)]

for i in range(n):
    for j in range(m):
        if plate[i][j] == 'X':
            plate[i][j] = 1
        else:
            plate[i][j] = 0

plate.insert(0, [0] * len(arr[0]))  # 맨 위에 길이만큼 0으로 이루어진 리스트 추가
plate.append([0] * len(arr[0]))     # 맨 아래에 길이만큼 0으로 이루어진 리스트 추가

for row in plate:
    row.insert(0, 0)  # 맨 왼쪽에 0 추가
    row.append(0)     # 맨 오른쪽에 0 추가

# 맨 위와 맨 아래에 0 추가

xy = [(0,-1),(0,1),(1,0),(-1,0)]

for i in range(1,n+1):
    for j in range(1,m+1):
        search(i,j)

num1 = 0
num2 = 0
while arr:
    if num1 < 1:
        for i in range(n+2):
            num1 += arr[i][0]
        if num1 == 0:
            for i in range(n+2):
                arr[i].pop(0)
        else:
            continue
    if num2 < 1:
        for i in range(n+2):
            num2 += arr[i][-1]
        if num2 == 0:
            for i in range(n+2):
                arr[i].pop()
        else:
            continue
    if num1 > 0 and num2 > 0:
        break
if not arr:
    print('X')
    quit()

num = 0
while num < 1:
    num = sum(arr[0])
    if num == 0:
        del(arr[0])

num = 0
while num < 1:
    num = sum(arr[-1])
    if num == 0:
        del(arr[-1])

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            arr[i][j] = '.'
        else:
            arr[i][j] = 'X'

for i in arr:
    print("".join(i))


