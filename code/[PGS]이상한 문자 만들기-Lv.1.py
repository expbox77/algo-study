'''
20230630
[PGS] 이상한 문자 만들기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12930
'''

s = ["try hello world"]
# return = ["TrY HeLlO WoRlD"]

sel_ex = 0
s_select = s[sel_ex]

def solution(s):
    temp_string = ""
    s = s.upper()

    for _ in s.split(" "):
        for i in range(len(_)):
            temp_string += _[i] if i % 2 == 0 else _[i].lower()
        temp_string += " "

    return temp_string[:-1]

print(solution(s_select))
