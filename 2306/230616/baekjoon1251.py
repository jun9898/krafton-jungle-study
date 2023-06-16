import sys
input = sys.stdin.readline

string = input().rstrip()
result = []
answer = []

for i in range(1,len(string)-1):
    for j in range(i+1, len(string)):
        a = string[:i]
        b = string[i:j]
        c = string[j:]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        result.append(a+b+c)

for a in result:
    answer.append(''.join(a))

print(sorted(answer)[0])

