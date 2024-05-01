import sys
input = sys.stdin.readline


def dp_recursive(x):
    if dp[x]:
        return dp[x]
    dp[x] = dp_recursive(x-2) + dp_recursive(x-3)
    return dp[x]


t = int(input())
dp = [0, 1, 1, 1] + ([0] * 97)

for _ in range(t):
    print(dp_recursive(int(input())))


