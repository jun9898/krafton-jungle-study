import sys
input = sys.stdin.readline

def calculate_digit_sum(string):
    result = 0
    for char in string:
        if char.isdigit():
            result += int(char)
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare_strings(arr[j], key) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def compare_strings(a, b):
    if len(a) != len(b):
        return len(a) - len(b)

    sum_a = calculate_digit_sum(a)
    sum_b = calculate_digit_sum(b)
    if sum_a != sum_b:
        return sum_a - sum_b

    return -1 if a < b else 1 if a > b else 0

n = int(input())
arr = [input().strip() for _ in range(n)]

insertion_sort(arr)

for string in arr:
    print(string)
