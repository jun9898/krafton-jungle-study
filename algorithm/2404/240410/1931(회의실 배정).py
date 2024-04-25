import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort(key=lambda x : (x[1], x[0]))
current = 0
cnt = 0
for i, j in room:
    if i < current:
        continue
    current = j
    cnt += 1
print(cnt)