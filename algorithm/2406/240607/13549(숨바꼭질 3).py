import sys
from collections import deque
input = sys.stdin.readline

limit = 100001
time = [0] * limit


def dp(n, m):
    queue = deque()
    if n == 0:
        queue.append(1)
    else:
        queue.append(n)
    while queue:
        cur_dist = queue.popleft()
        if cur_dist == m:
            return time[cur_dist]
        for new_dist in (cur_dist-1, cur_dist+1, cur_dist * 2):
            if 0 <= new_dist < limit and 0 == time[new_dist]:
                if new_dist == cur_dist * 2:
                    time[new_dist] = time[cur_dist]
                    queue.appendleft(new_dist)
                else:
                    time[new_dist] = time[cur_dist] + 1
                    queue.append(new_dist)


n, m = map(int, input().split())

if n==0:
    if m==0:
        print(0)
    else:
        print(dp(n,m)+1)
else :
    print(dp(n,m))




