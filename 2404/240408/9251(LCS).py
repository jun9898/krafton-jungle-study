import sys
input = sys.stdin.readline

LCS_patten1 = input().rstrip()
LCS_patten2 = input().rstrip()

# 두 문자열의 길이
m = len(LCS_patten1)
n = len(LCS_patten2)

# LCS를 구하기 위한 DP 테이블 초기화
dp_table = [[0] * (n + 1) for _ in range(m + 1)]

# LCS를 구하는 과정
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if LCS_patten1[i-1] == LCS_patten2[j-1]:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
        else:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

# LCS의 길이 출력
print(dp_table[m][n])
