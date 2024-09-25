import sys
input = sys.stdin.readline

n = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [0] * 100
for h, p in zip(health, happy):
    for j in range(99, h - 1, -1):
        dp[j] = max(dp[j], dp[j - h] + p)

print(dp[99])
