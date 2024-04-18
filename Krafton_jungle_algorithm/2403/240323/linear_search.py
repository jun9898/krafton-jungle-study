def linear_search(arr, i):
    for j in arr:
        if j == i:
            return True

arr = [1,2,3,4,6,8,11,10,12,13,14,15,16,17,18,19]
i = 10

print(linear_search(arr, i))

