n = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(n+1)] # 제곱수는 1로 저장

res = 4
for i in range(int(n**0.5), 0, -1):
    if arr[n] :
        res=1
        break
    elif arr[n-i**2] :
        res=2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if arr[(n-i**2)-j**2]: # 제곱수를 한번 더 뺀 나머지가 제곱수일 경우
                res=3
print(res)
