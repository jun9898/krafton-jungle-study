# # def solution(name, yearning, photo):
# name = 	["may", "kein", "kain", "radi"]
# nameList = [i for i in name]
# score = {nameList:15}
# print(nameList)
    
def solution(name, yearning, photo):
    result = []
    info = dict(zip(name,yearning))
    
    for peple in photo:
        score = 0
        for person in peple:
            score += info.get(person, 0)
        result.append(score)
    
    return result