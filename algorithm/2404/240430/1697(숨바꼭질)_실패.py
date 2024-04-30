import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = set()
main_deque = deque([n])
count = 0

if n == k:
    print(0)
    sys.exit()

while True:
    sub_deque = deque(main_deque)
    count += 1
    print(count)
    while sub_deque:
        cur = sub_deque.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        for tmp in [cur - 1, cur + 1, cur * 2]:
            if tmp == k:
                print(count)
                sys.exit()
            elif tmp not in visited:
                main_deque.append(tmp)
