a, b = map(int,input().split())

m = int(input())

arr = list(map(int,input().split()))
arr.reverse()

result = 0
for i in range(m):
    result += arr[i]*(a**i)

answer = []
while result//b:
    answer.append(result%b)
    result = result//b
answer.append(result)

answer.reverse()

print(" ".join(map(str,answer)))
    

