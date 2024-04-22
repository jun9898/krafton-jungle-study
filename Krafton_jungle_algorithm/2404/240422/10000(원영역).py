import sys

input = sys.stdin.readline

n = int(input())

tmp_arr = []
stack = []

for i in range(n):
    x, r = map(int, input().split())
    tmp_arr.append([x - r, 1, "("])
    tmp_arr.append([x + r, 0, ")"])

tmp_arr.sort()

res = 0

for cur in tmp_arr:
    if cur[2] == "(":
        stack.append(cur)
    if cur[2] == ")":
        prev = stack.pop()
        prev_distance = 0
        while prev[0] is None:
            prev_distance += prev[1]
            prev = stack.pop()
        if prev_distance == cur[0] - prev[0]:
            res += 2
            stack.append([None, prev_distance])
        else:
            res += 1
            stack.append([None, cur[0] - prev[0]])
    print(res)
# 외부영역 +1
print(res + 1)
