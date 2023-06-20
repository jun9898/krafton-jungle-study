from collections import Counter
n = int(input())
arr = [list(input())for _ in range(n)]

answer = 0

for i in range(len(arr[0])-1, -1, -1):
    result = []
    count = 0
    for j in range(n):
        string = "".join(arr[j][i:])
        result.append(string)
    answer += 1
    result = Counter(result)
    for i,j in result.items():
        if int(j) > 1:
            count += 1
    if count < 1:
        print(answer)
        quit()

     

