import sys
from collections import defaultdict

input = sys.stdin.readline

def solve(n, k, work, efficiency):
    count = 0
    current_count1 = current_count2 = 0
    current_sum1 = current_sum2 = 0
    prefix_diff = defaultdict(list)
    prefix_diff[0].append((0, 0))

    for i in range(n):
        if work[i] == 1:
            current_count1 += 1
            current_sum1 += efficiency[i]
        elif work[i] == 2:
            current_count2 += 1
            current_sum2 += efficiency[i]

        diff = current_count1 - current_count2

        for prev_sum1, prev_sum2 in prefix_diff[diff]:
            if abs((current_sum1 - prev_sum1) - (current_sum2 - prev_sum2)) <= k:
                count += 1

        prefix_diff[diff].append((current_sum1, current_sum2))

    return count

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    work = list(map(int, input().split()))
    efficiency = list(map(int, input().split()))

    result = solve(n, k, work, efficiency)
    print(result)
