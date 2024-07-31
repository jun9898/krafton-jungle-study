import sys
input = sys.stdin.readline

n, m = map(int,input().split())
key = min(n,m)

arr = list(list(map(int,input().rstrip())) for _ in range(n))

def check(y):
    for i in range(n-y+1):
        for j in range(m-y+1):
            if arr[i][j] == arr[i][j+y-1] == arr[i+y-1][j] == arr[i+y-1][j+y-1]:
                return True
    
    return False

for i in range(key,0,-1):
    if check(i):
        print(i**2)
        break



