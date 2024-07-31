
def javaToC(n):
    error = "Error!"

    result = []
    for i in range(len(n)):
        if n[i].isupper():
            if i == 0:
                return error
            else:
                result.append(f'_{n[i].lower()}')
        else:
            result.append(n[i].lower())
    return "".join(result)

def cToJava(n):
    error = "Error!"

    result = []
    if '__' in n:
        return error
    if n[0] == '_' or n[-1] == '_':
        return error
    if not n.islower():
        return error
    for i in n.split('_'):
        if not result:
            result.append(i)
        else:
            result.append(i.capitalize())
    return "".join(result)

n = input()

if '_' in n:
    print(cToJava(n))
else:
    print(javaToC(n))


