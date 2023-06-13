import sys; input = sys.stdin.readline

result = ''
string = input().rstrip().split('.')
for i in string:
    if len(i)%2 == 0:
        n = len(i) // 4
        m = (len(i) - (n*4)) // 2
        result += "AAAA" * n
        result += "BB" * m
        result += '.'
    else:
        print(-1)
        quit()
print(result[0:-1])
