# T = int(input())
# listCoin = [25, 10, 5, 1]
# for i in range(T):
#     num = int(input())
#     listT = []
#     for j in range(4):
#         coin = num // listCoin[j]
#         num -= listCoin[j] * coin
#         listT.append(coin)
#     print(*listT)

# T = int(input())
# get_money = [int(input()) for i in range(T)]
# put_money = [25,10,5,1]
# result = [[0]*4 for i in range(T)]

# for g in range(len(get_money)):
#     for p in range(len(put_money)):
#         result[g][p] = get_money[g] // put_money[p]
#         get_money[g] %= put_money[p]

# for ret in result:
#     print(*ret)

print((2**int(input())+1)**2)