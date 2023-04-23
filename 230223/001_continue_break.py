


from random import randint
hands = {0:"가위",1:"바위",2:"보"}
rules = {(0,0):"비김",(0,1):"win",(0,2):"lose",
         (1,0):"lose",(1,1):"비김",(1,2):"win",
         (2,0):"win",(2,1):"lose",(2,2):"비김",}

while True:
    pc_hand = randint(0,2)
    user_hand = input("0 가위 1 바위 2 보 3 종료")

    if user_hand == "3":
        break
    if user_hand not in ('0','1','2'):
        continue
    user_hand_int = int(user_hand)
    print ("당신 : "+ hands[user_hand_int], "상대 : "+ hands[pc_hand])
    print (rules[pc_hand,user_hand_int])