import sys
input = sys.stdin.readline

def back_track(tmp_arr):
    if len(tmp_arr) == m:
        print(*tmp_arr)
        return
    for i in range(len(arr)):
        tmp_arr.append(arr[i])
        back_track(tmp_arr)
        tmp_arr.pop()

n, m = map(int, input().split())
arr = sorted(dict.fromkeys(map(int, input().split())))

back_track([])