# def draw1(h):
#     if (h==0):
#         return
#     draw1(h-1)
#     i = 0
#     while i<h:
#         print("*", end="")
#         i+=1
#     print()

# def draw2(h):
#     o = 0
#     while o<h:
#         i = 0
#         while i < o:
#             print("*", end="")
#             i+=1
#         o+=1
#         print()

# draw1(5)
# draw2(5)

# 딕셔너리의 key와 values로 풀어보았다. 
arr = [6,5,5,6,6,6,5,5,4,4,3,2,1]
dic = dict()

def countDic(arr):
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    result = []

    for d in dic:
        if dic[d] != 1:
            result.append(dic[d])

    if len(result) == 0:
        return -1
    else:
        return result

print(countDic(arr))
