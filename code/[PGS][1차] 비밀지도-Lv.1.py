'''
20230711
[1차] 비밀지도 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/17681
'''

# 입출력 예
n = [5, 6]
arr1 = [[9, 20, 28, 18, 11], [46, 33, 33 ,22, 31, 50]]
arr2 = [[30, 1, 21, 17, 28], [27 ,56, 19, 14, 14, 10]]
# result = [["#####", "# # #", "### #", "# ##", "#####"], ["######", "### #", "## ##", " #### ", " #####", "### # "]]

sel_ex = 1
n_select = n[sel_ex]
arr1_select = arr1[sel_ex]
arr2_select = arr2[sel_ex]


def solution(n, arr1, arr2):
    res = ["" for i in range(n)]

    for _ in range(n):
        for i, j in zip(bin(arr1[_])[2:].zfill(n), bin(arr2[_])[2:].zfill(n)):
            res[_] += "#" if bool(int(i)) or bool(int(j)) else " "

    return res

# print(solution(n_select, arr1_select, arr2_select))

print(type(bin(9)))
