arrNum = list(list(map(int, input().split())) for _ in range(5))
arrBingo = list(list([0]*5) for _ in range(5))
callBingo = list(list(map(int, input().split())) for _ in range(5))

gCount = 0
def check(n):
    global gCount
    gCount += 1
    # 숫자 체크
    for i in range(5):
        for j in range(5):
            if arrNum[i][j] == n:
                arrBingo[i][j] = 1
    count = 0
    # X 체크
    for x in range(5):
        if sum(arrBingo[x]) == 5:
            count += 1
    
    # Y 체크
    for y in range(5):
        result = 0
        for x in range(5):
            result +=  arrBingo[x][y]
        if result == 5:
            count += 1
    # 대각 체크
    result = 0
    for y in range(5):
        result += arrBingo[y][y]
    if result == 5:
        count += 1

    result = 0
    for y in range(4, -1, -1):
        result += arrBingo[y][4-y]
    if result == 5:
        count += 1
    
    if count >= 3:
        print(gCount)
        quit()
        
            

        

    # 대각 체크


            
            


for i in range(5):
    for j in range(5):
        check(callBingo[i][j])