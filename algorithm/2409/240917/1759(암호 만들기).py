import sys
input = sys.stdin.readline

def is_vowel(letter):
    vowels = "aeiou"
    return letter in vowels

def dfs(arr, index, consonant, vowel):
    if len(arr) == l:
        if consonant < 2 or vowel < 1:
            return
        else:
            print("".join(arr))
            return
    for i in range(index, c):
        arr.append(password[i])
        if is_vowel(arr[-1]):
            dfs(arr, i + 1, consonant, vowel+1)
        else:
            dfs(arr, i + 1, consonant + 1, vowel)
        arr.pop()

l, c = map(int, input().split())
password = list(input().rstrip().split())
password.sort()

dfs([], 0, 0, 0)



