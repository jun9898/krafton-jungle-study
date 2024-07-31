n = int(input())



def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        print(1, count)
        return 1 
    elif s[l] != s[r]:
        print(0, count)
        return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for i in range(n):
    string = input()
    count = 0
    isPalindrome(string)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))