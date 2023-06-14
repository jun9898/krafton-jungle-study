n = int(input())

answer = []
if n%10 == 0:

    a = n//300
    answer.append(a)
    n -= a*300

    b = n//60
    answer.append(b)
    n -= b*60

    c = n//10
    answer.append(c)
    n -= c*10
else:
    print(-1)
    quit()
print(*answer)
        