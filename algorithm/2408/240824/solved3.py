import sys
input = sys.stdin.readline

def max_dolphins_dp(N, K, M):
    dp = [[-1] * (1 << N) for _ in range(K + 1)]
    dp[0][0] = 0  # 시작 상태

    for t in range(K):
        for cam in range(1 << N):
            if dp[t][cam] == -1:
                continue

            dp[t + 1][cam] = max(dp[t + 1][cam], dp[t][cam])

            for i in range(N):
                new_cam = cam | (1 << i)
                dp[t + 1][new_cam] = max(dp[t + 1][new_cam], dp[t][cam])

            for i in range(N):
                if cam & (1 << i) and M[i][t] == 1:
                    dp[t + 1][cam] = max(dp[t + 1][cam], dp[t][cam] + 1)

    return max(dp[K])

N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]

print(max_dolphins_dp(N, K, M))
