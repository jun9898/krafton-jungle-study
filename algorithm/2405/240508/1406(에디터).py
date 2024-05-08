import sys
from collections import deque
input = sys.stdin.readline

tmp = list(input().rstrip())
tmp_left = deque(tmp)
tmp_right = deque()

n = int(input())

for i in range(n):
    commend = list(input().rstrip().split())
    total_len = len(tmp)
    if commend[0] == 'L' and tmp_left:
        tmp_right.appendleft(tmp_left.pop())
    elif commend[0] == 'D' and tmp_right:
        tmp_left.append(tmp_right.popleft())
    elif commend[0] == 'B' and tmp_left:
        tmp_left.pop()
    elif commend[0] == 'P':
        tmp_left.append(commend[1])
print("".join(map(str, tmp_left + tmp_right)))

