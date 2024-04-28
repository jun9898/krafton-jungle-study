import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[0] == 0 and arr[0] == 0:
        break
    max_num = max(arr)**2
    num_arr = []
    for i in arr:
        if max_num > i**2:
            num_arr.append(i**2)
    if max_num == sum(num_arr):
        print("right")
        continue
    print("wrong")







