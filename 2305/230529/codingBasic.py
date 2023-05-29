# import random

# count = 1

# setPw = random.randint(1,5)

# def freq(name):
#     pw = int(input("pw(1~5) = "))

#     if count == 4:
#         print("time over")
#         exit()

#     if pw == setPw:
#         print("login 성공", name, "님 입장")
#         exit()
#     else:
#         print("retry")

# name = input("name ")

# while True:
#     if count == 4:
#         print("time over")
#         break
#     count += 1
#     freq(name)

def slot(coin):
    while True:
        if coin < 600:
            print("insert coin more")
            coin += int(input("insert coin : "))
        else:
            print("음료를 선택하세요\n 1.밀크티(700) 2.힘찬드링크(800) 3. 아이스티(600) 4.잔돈받기")
            n = int(input())
            if n == 1 and coin >= 700:
                coin -= 700
                print("밀크티 나왔습니다")
                print("딩동!"*(coin//100), coin, "원을 돌려받았다")
                continue
            if n == 2 and coin >= 800:
                coin -= 800
                print("힘찬드링크 나왔습니다")
                print("딩동!"*(coin//100), coin, "원을 돌려받았다")
                continue
            if n == 3 and coin >= 600:
                coin -= 600
                print("아이스티 나왔습니다")
                print("딩동!"*(coin//100), coin, "원을 돌려받았다")
                continue
            if n == 4:
                print("딩동!"*(coin//100), coin, "원을 돌려받았다")
                return coin
            else:
                print("coin 이 부족합니다")
                coin += int(input("insert coin"))

coin = int(input("insert coin : "))
slot(coin)
print(coin)