n, k = map(int, input().split())

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
    

print(fac(n) // (fac(n-k) * fac(k)))
