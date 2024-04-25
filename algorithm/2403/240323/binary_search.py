def binary_search(arr, i):
    mid = len(arr)//2
    if mid < 1:
        return False
    elif arr[mid] < i:
        return binary_search(arr[mid:], i)
    elif arr[mid] > i:
        return binary_search(arr[:mid], i)
    if arr[mid] == i:
        return True



i = 9
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
total = len(arr)
print(binary_search(arr, i))
