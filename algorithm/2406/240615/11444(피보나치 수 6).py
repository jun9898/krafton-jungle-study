def F(num):
    if num <= 2:
        return memo[num]
    elif memo[num] > 0:
        return memo[num]
    else :
        half = num //2
        if num % 2 == 0 :
            h0 = F(half)
            h1 = F(half-1)
            memo[num] = ((2*h1 + h0)*h0)%1000000007
            return memo[num]
        else :
            h0 = F(half+1)
            h1 = F(half)
            memo[num] = (h0**2 + h1**2)%1000000007
            return memo[num]

from collections import defaultdict
n = int(input())
memo = defaultdict(int)
memo[1],memo[2] = 1,1
print(F(n))

# 출처 : https://velog.io/@kjy2134/%EB%B0%B1%EC%A4%80-11444-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
