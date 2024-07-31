from collections import deque


def ro(arr):
    arr2 = []
    for _ in range(4):
        arr.rotate(1)
        arr2.append(int("".join(arr)))
    answer = min(arr2)
    return answer

count = 0

arr = deque(map(str,input().split()))
arr = ro(arr)

for i in range(1111,arr+1):
    if '0' not in list(str(i)) and i == ro(deque(str(i))):
        count+=1
print(count)
