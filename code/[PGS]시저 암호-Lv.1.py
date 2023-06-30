'''
20230630
[PGS] 시저 암호 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12926
'''

# 입출력 예
s = ["AB", "z", "a B z"]
n = [1, 1, 4]
# result = ["BC", "a", "e F d"]

sel_ex = 1
s_select = s[sel_ex]
n_select = n[sel_ex]

def solution(s, n):
    down_alpha = sorted("qwertyuiopasdfghjklzxcvbnm")
    up_alpha = sorted("QWERTYUIOPASDFGHJKLZXCVBNM")
    temp_str = ""

    for _ in s:
        if _ == " ":
            temp_str += " "
            continue
        if _.isupper():
            temp_str += up_alpha[(up_alpha.index(_) + n) % len(up_alpha)]
        else:
            temp_str += down_alpha[(down_alpha.index(_) + n) % len(down_alpha)]
    return temp_str

print(solution(s_select, n_select))
