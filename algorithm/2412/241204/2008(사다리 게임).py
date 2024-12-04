import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, X, Y = map(int, input().split())
a -= 1
b -= 1
ladders = [0] * (m + 1)

for i in range(1, m + 1):
    ladders[i] = int(input()) - 1

dp = [[math.inf] * n for _ in range(m + 1)]

for i in range(n):
    if i == a:
        dp[0][i] = 0
    else:
        dp[0][i] = abs(a - i) * Y

for i in range(1, m + 1):
    for j in range(n):
        for k in range(n):
            if k == j and (ladders[i] == k or ladders[i] + 1 == k):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + X)
            elif (k <= ladders[i] <= j - 1) or (j <= ladders[i] <= k - 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + (abs(k - j) - 1) * Y)
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(k - j) * Y)

print(dp[m][b])