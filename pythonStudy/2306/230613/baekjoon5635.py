import sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    n,d,m,y = input().rstrip().split()
    d,m,y = map(int,(d,m,y))
    arr.append((y,m,d,n))
arr.sort()
print(arr[-1][3])
print(arr[0][3])


    



