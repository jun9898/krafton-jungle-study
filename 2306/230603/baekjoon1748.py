import sys
input = sys.stdin.readline
"""
https://dlog0518.tistory.com/37
풀이 참고함 아직 완벽하게 이해 못했음
"""
n = int(input())
count = len(str(n))

result = 0
for i in range(1,count):
    result += (10**(i)-10**(i-1))*i
result += ((n+1)-10**(count-1))*(count)

print(result)