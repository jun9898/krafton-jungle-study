import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    dp_size = int(input())
    dp_table = [0 for _ in range(dp_size + 1)]
    dp_table[0] = 1
    for coin in coins:
        for i in range(coin, dp_size+1):
            dp_table[i] = (dp_table[i] + dp_table[i - coin])
    print(dp_table[-1])
