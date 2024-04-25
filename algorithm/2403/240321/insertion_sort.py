def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

arr = [1,3,5,7,4,2,6]
print(insertion_sort(arr))