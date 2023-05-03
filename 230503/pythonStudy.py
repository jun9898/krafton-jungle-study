# import math
# print(math.gcd(60, 100, 80, 3))
# print(math.lcm(1,2,3,4,5,6,7,8,9,10))

####################

# import itertools
# print(len(list(itertools.combinations_with_replacement(range(1,46), 6))))

####################

# import time
# import threading

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)

# print("Start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join()

# print("End")

###################

# import traceback
# def a():
#     return 1/0
# def b():
#     a()
# def main():
#     try:
#         b()
#     except:
#         print("오 류 발 생")
#         print(traceback.format_exc())
# main()

###################

# import urllib.request

# def get_wikidocs(page):
#     resource = 'http://wikidocs.net/{}'.format(page)
#     with urllib.request.urlopen(resource) as s:
#         with open('wikidocs_%s.html' % page, 'wb') as f:
#             f.write(s.read())

# get_wikidocs(5) # result = wikidocs_5.html

###################

