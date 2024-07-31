import sys
input = sys.stdin.readline

# 반복할 횟수 입력
n = int(input())

# 덩치 정보를 2차원 배열로 설정
listD = list(list(map(int, input().split())) for _ in range(n))


# 배열에 있는 값들로 for문을 돌려준다
for i in listD:
    # 기준이 될 rank값을 설정해준다
    rank = 1
    # list[i]와 비교할 list[j] 값을 설정해준다.
    for j in listD:
        # 만약 list[i]의 값이 모두 list[j]값보다 작으면 rank에 1을 더해준다.
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    # 루프가 돌때마다 rank를 print.
    print(rank, end=" ")


