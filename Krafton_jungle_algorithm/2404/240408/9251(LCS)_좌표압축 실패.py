import sys
input = sys.stdin.readline

LCS_patten1 = input().rstrip()
LCS_patten2 = input().rstrip()

if len(LCS_patten1) > len(LCS_patten2):
    LCS_patten1, LCS_patten2 = LCS_patten2, LCS_patten1

# print("길이가 더 짧은 문자열:", LCS_patten1, len(LCS_patten1))
# print("길이가 더 긴 문자열:", LCS_patten2, len(LCS_patten2))

dp_table = [0] * (len(LCS_patten2) + 1)

for i in range(1, len(LCS_patten1) + 1):
    for j in range(1, len(LCS_patten2) + 1):
        if LCS_patten1[i-1] == LCS_patten2[j-1]:
            dp_table[j] = dp_table[j-1] + 1
        else:
            dp_table[j] = max(dp_table[j], dp_table[j-1])

print(dp_table[-1])



