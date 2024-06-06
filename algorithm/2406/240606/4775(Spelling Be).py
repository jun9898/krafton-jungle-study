import sys
input = sys.stdin.readline

document = set()

for i in range(int(input().strip())):
    document.add(input().strip())


def check_spelling(dictionary, emails, num):
    unknown_words = []
    for email in emails:
        if email not in dictionary:
            unknown_words.append(email)
    if unknown_words:
        print(f"Email {num} is not spelled correctly.")
        for word in unknown_words:
            print(word)
    else:
        print(f"Email {num} is spelled correctly.")


num_of_email = int(input().strip())
for i in range(1, num_of_email + 1):
    emails = []
    while True:
        tmp = input().strip()
        if tmp == "-1":
            break
        else:
            emails.append(tmp)
    check_spelling(document, emails, i)

print("End of Output")
