import sys
input = sys.stdin.readline

a, p = input().split()

flag = True

arr = []
arr2 = []

arr.append(a)

while True:
    if flag:
        result = 0
        for i in a:
            num = int(i)
            result += num**int(p)
        if str(result) in arr:
            flag = False
            arr2.append(str(result))
            a = str(result)
            continue
        arr.append(str(result))
        a = str(result)
    else:
        result = 0
        for i in a:
            num = int(i)
            result += num**int(p)
        if str(result) in arr2:
            break
        arr2.append(str(result))
        a = str(result)
print(len(arr) - len(arr2))

# a, p = map(int,input().split())

# nums = [a]
# while True:
#     tmp = 0
#     for s in str(nums[-1]):
#         tmp += int(s) ** p
    
#     if tmp in nums:
#         break

#     nums.append(tmp)

# print(nums.index(tmp))





