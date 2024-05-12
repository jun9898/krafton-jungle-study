import sys
input = sys.stdin.readline

n = int(input())
tmp = input().rstrip()

values = []
for i in range(n):
    values.append(int(input()))

stack = []
for i in tmp:
    ascii_input = ord(i)
    if 65 <= ascii_input <= 90:
        stack.append(values[ascii_input-65]) # 해당 value 저장
    elif ascii_input == 43: # + = 43
        cur1 = stack.pop()
        cur2 = stack.pop()
        stack.append(cur1 + cur2)
    elif ascii_input == 45: # - = 45
        cur1 = stack.pop()
        cur2 = stack.pop()
        stack.append(cur2 - cur1)
    elif ascii_input == 47: # / = 47
        cur1 = stack.pop()
        cur2 = stack.pop()
        stack.append(cur2 / cur1)
    elif ascii_input == 42: # * = 42
        cur1 = stack.pop()
        cur2 = stack.pop()
        stack.append(cur1 * cur2)

result = "%.2f" % stack.pop()
print(result)





