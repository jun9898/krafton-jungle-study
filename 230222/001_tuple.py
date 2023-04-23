month_name = ("january", "february", "march", "april", "may", "june", "july")

print(month_name[1]) #튜플은 리스트와 헷갈릴 수 있으나 요소의 변경이 불가능합니다.

month_name0 = month_name + ("august", "september")
print(month_name0[7])   #튜플은 수정은 불가능하나 다른 튜플과 합성하여 새로운 튜플을 작성할 수 있습니다.

print(month_name0[2:7])

pref_0 = {(37.27479,127.00962):"경기도",
          (37.88565,127.73):"강원도",
          (36.48008,127.28921):"서울시",}
# loc = (36.48008,127.28921)
# for key in pref_0:
#     if key == loc:
#         print (pref_0[key])
#         break

loc = (36,127)
nearest_cap = ''
nearest_dist = 10000

for key in pref_0:
    dist = (loc[0]-key[0])**2 + (loc[1]-key[1])**2
    if nearest_dist > dist:
        nearest_dist = dist
        nearest_cap = pref_0[key]

print(nearest_cap)