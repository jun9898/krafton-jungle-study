n = int(input())

dic = dict()
for i in range(n):
    선수 = list(map(int, input().split()))
    dic[(선수[0],선수[1])] = 선수[2]

result = dict(sorted(dic.items(), key= lambda x:x[1], reverse=True))

medalCount = [0]*n

answer = []
count = 0
for key, value in result.items():
    if count < 3:
        if medalCount[key[0]] < 2:
            answer.append(key)
            count += 1
            medalCount[key[0]] += 1
    else:
        break

for i in answer:
    print(*i)
    

