import sys
input = sys.stdin.read

N, *S = input().split()
for i in range(int(N)):
    S[i] = S[i][::-1]
S = list(map(int, S))
print(*sorted(S), sep="\n")
