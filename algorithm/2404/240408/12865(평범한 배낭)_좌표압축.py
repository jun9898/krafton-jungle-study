import sys
input = sys.stdin.readline

n, k = map(int, input().split())

wv_list = []
for _ in range(n):
    wv_list.append(list(map(int, input().split())))

dp_table = [0]*(k+1)

# 좌표 압축
for w, v in wv_list:
    if w > k:
        continue
    for j in range(k, w-1, -1):
        dp_table[j] = max(dp_table[j], dp_table[j - w] + v)

print(dp_table[k])

