import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w
answer = 0

left_max[0] = block[0]
for i in range(1, w):
    left_max[i] = max(left_max[i - 1], block[i])

right_max[w - 1] = block[w - 1]
for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], block[i])

for i in range(1, w - 1):
    m = min(left_max[i], right_max[i])
    if m > block[i]:
        answer += m - block[i]

print(answer)
