import sys

input = sys.stdin.readline

tmp = input().rstrip()
stack = []
ppap = ["P", "P", "A", "P"]

for i in range(len(tmp)):
    stack.append(tmp[i])
    if stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")



