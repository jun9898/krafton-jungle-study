from collections import defaultdict

def int_append():
    return "########"


def padding_dot(string1):
    while len(string1) != 8:
        string1 += "."
    return string1

def solve(arr):
    return_arr = [""]
    for arr_one in arr:
        if len(return_arr[-1]) == 8:
            return_arr.append("")
        if arr_one == "LONG":
            if return_arr[-1] == "":
                return_arr.pop()
                return_arr.append("########")
                return_arr.append("########")
            else:
                return_arr.append(padding_dot(return_arr.pop()))
                return_arr.append("########")
                return_arr.append("########")
        elif arr_one == "INT":
            if return_arr[-1] == "":
                return_arr.pop()
                return_arr.append("########")
            else:
                return_arr.append(padding_dot(return_arr.pop()))
                return_arr.append("########")

        elif arr_one == "FLOAT":
            if len(return_arr[-1]) >4:
                return_arr.append(padding_dot(return_arr.pop()))
                return_arr.append("####")
            else:

                while 1:
                    if not (len(return_arr[-1]) % 4):
                        break
                    return_arr[-1] += "."
                return_arr[-1] += "####"

        elif arr_one == "SHORT":
            if len(return_arr[-1]) >6:
                return_arr.append(padding_dot(return_arr.pop()))
                return_arr.append("##")
            else:
                while 1:
                    if not (len(return_arr[-1]) % 2):
                        break
                    return_arr[-1] += "."
                return_arr[-1] += "##"
        elif arr_one == "BOOL":
            return_arr[-1] += "#"


    if len(return_arr) > 16:
        return_val = "HALT"
    else:
        #마지막 메모리 패딩
        while 1:
            if len(return_arr[-1]) == 8:
                break
            return_arr[-1] += "."
        #사이 쉼표 패딩
        return_val = ",".join(return_arr)
    print(return_val)
    return return_val

if __name__ == '__main__':

    test1 = ["INT", "INT", "BOOL", "SHORT", "LONG"]
    ans1 = "########,########,#.##....,########,########"

    test2 = ["INT", "SHORT", "FLOAT", "INT", "BOOL"]
    ans2 = "########,##..####,########,#......."

    test3 = ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]
    ans3 = "########,#.......,########"

    test4 = ["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"]
    ans4 = "HALT"
    test_arr = [test1, test2, test3, test4]
    ans_arr = [ans1, ans2, ans3, ans4]

    for idx in range(len(test_arr)):
        if solve(test_arr[idx]) == ans_arr[idx]:
            print(f"{idx}번 테스트 성공")
        else:
            print(f"{idx}번 테스트 실패")
