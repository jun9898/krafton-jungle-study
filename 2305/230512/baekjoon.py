# 내가 생각한 숫자를 말하기

# 만약 정답이라면 게임 끝내기

# 만약 내가 말한 숫자가 크다면 
#     1부터 내가 말한 숫자의 범위의 절반값 말하기
#     3번부터 반복하기

# 만약 아니라면
#     내가 말한 숫자부터 100까지의 절반값 말하기
#     3번부터 반복하기

while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    elif y % x == 0:
        print("factor")
    elif x % y == 0:
        print("multiple")
    else:
        print("neither")


