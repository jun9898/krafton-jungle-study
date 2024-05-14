import sys
input = sys.stdin.readline

input_string = input().rstrip()

arr = []

for i in range(len(input_string)):
    arr.append(input_string[i:])

arr.sort()

for i in arr:
    print(i)