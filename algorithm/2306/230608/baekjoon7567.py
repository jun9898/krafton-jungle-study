import sys
input = sys.stdin.readline

n = list(input().rstrip())
result = 10

for i in range(len(n)):
    try:
        if n[i] == n[i+1]:
            result += 5
        else:
            result += 10
    except:
        break

print(result)