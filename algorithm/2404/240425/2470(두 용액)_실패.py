import sys
input = sys.stdin.readline
min = sys.maxsize


def binary_search(arr, target_value):
    if len(arr) == 1:
        # 값과 target value, 중간값 리턴
        return abs(target_value+arr[0]), target_value, arr[0]
    mid = len(arr)//2
    if target_value + arr[mid] == 0 and target_value != 0:
        return abs(target_value+arr[mid]), target_value, arr[mid]
    elif target_value + arr[mid] < arr[mid]:
        return binary_search(arr[mid:], target_value)
    elif target_value + arr[mid] > arr[mid]:
        return binary_search(arr[:mid], target_value)


n = int(input())
arr = list(map(int, input().split()))
arr.sort()


result_arr = []
for i in range(n):
    if arr[i] == 0:
        prev = arr[i-1]
        sub = arr[i+1]

        tmp = 0
        if abs(prev) < abs(sub):
            tmp = prev
        else:
            tmp = sub
        result_arr.append((tmp+arr[i], arr[i], tmp))
    else:
        result = (binary_search(arr,arr[i]))
        if result[0] == 0:
            print(result[1], result[2])
            exit(0)
        else:
            result_arr.append(result)

result_arr.sort()
print(result_arr[0][1],result_arr[0][2])


