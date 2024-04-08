import sys
input = sys.stdin.readline

n, k = map(int, input().split())

wv_list = [[0, 0]]

for _ in range(n):
    wv_list.append(list(map(int, input().split())))

dp_table = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = wv_list[i][0]
        value = wv_list[i][1]

        # 만약 무게가 j보다 작으면
        if j < weight:
            dp_table[i][j] = dp_table[i-1][j]
        else:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-weight] + value)

print(dp_table[n][k])

