import sys
input = sys.stdin.readline

array = list()

n = int(input())

for i in range(n):
    array.append(int(input()))

result = 0
count = 0
while array:
    i = array.pop()
    if i > result:
        count += 1
        result = i
print(count)
