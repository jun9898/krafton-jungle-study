
Americano = 1
Americano_Price = 2000
Latte = 1
Latte_Price = 3000
myPocket = 100000
while True:
    coin = int(input("insert coin : "))
    myPocket -= coin
    if myPocket < 0:
        myPocket += coin
        print("돈이 없습니다.")
        continue
    print("잔액 : ", myPocket)
    order = int(input("""1. Americano : 2000\n2. Latte     : 3000\n3. break\nselect number: """))
    if order == 1:
        if Americano == 0:
            print("No more Americano.")
            continue
        elif coin < Americano_Price:
            print("잔액이 부족합니다")
            myPocket += coin
        else:
            coin -= Americano_Price
            print("Americano here")
            Americano -= 1
            myPocket += coin
            print(f'{myPocket} in my poket')

    if order == 2:
        if Latte == 0:
            print("No more Americano.")
            continue
        if coin < Latte_Price:
            print("잔액이 부족합니다")
            myPocket += coin
        else:
            coin -= Latte_Price
            print("Latte here")
            Latte -= 1
            myPocket += coin
            print(f'{myPocket} in my poket')

    if order == 3: break

    if Americano == 0 and Latte == 0:
        print("재료 소진")    
        break

