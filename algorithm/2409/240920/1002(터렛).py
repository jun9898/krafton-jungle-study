import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dis_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

    sum_r_sq = (r1 + r2) ** 2
    diff_r_sq = (r1 - r2) ** 2

    if dis_sq == 0:
        print(-1 if r1 == r2 else 0)
    elif diff_r_sq <= dis_sq <= sum_r_sq:
        print(1 if dis_sq in (diff_r_sq, sum_r_sq) else 2)
    else:
        print(0)