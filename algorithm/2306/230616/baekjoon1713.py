import sys
input = sys.stdin.readline

def find_key(dic, v):
    for key, value in dic.items():
        if value == v:
            return key


n = int(input())
result = []

k = int(input())

dic = dict()
arr = map(int,input().split())

for i in arr:
    if len(result) < n:
        if i not in result:
            result.append(i)
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    else:
        if i in dic:
            dic[i] += 1
        else:
            m = find_key(dic, min(dic.values()))
            dic.pop(m)
            idx = result.index(m)
            result.pop(idx)

            result.insert(idx, i)
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

result.sort()
print(*result)

