import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict_site = dict()
for i in range(n):
    tmp_site, password = input().rstrip().split()
    dict_site[tmp_site] = password

for i in range(m):
    print(dict_site[input().rstrip()])
