import sys
input = sys.stdin.readline

result = 0

string_list = list(map(str, input().rstrip().split("-")))

for i in string_list[0].split("+"):
    result += int(i)

for i in string_list[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)
