import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(len(arr[i])):
        if j==0:
            arr[i][j]=arr[i][j]+arr[i-1][j]
        elif j==len(arr[i])-1:
            arr[i][j]=arr[i][j]+arr[i-1][j-1]
        else:
            arr[i][j]=max(arr[i-1][j-1],arr[i-1][j])+arr[i][j]

print(max(arr[n-1]))
# 출처 https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95