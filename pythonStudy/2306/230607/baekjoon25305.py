n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort(reverse=True)
print(array[m-1])