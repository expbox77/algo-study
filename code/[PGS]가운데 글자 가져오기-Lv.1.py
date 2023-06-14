'''
20230614
[PGS] 가운데 글자 가져오기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12903
'''

s = ["abcde", "qwer", "qw"]
# return = ["c", "we", "qw"]

# 입출력 예 1
s_select = s[0]

def solution(s):
    center_num = int(len(s) / 2)
    
    if len(s) % 2 == 0:
        return s[center_num - 1 : center_num + 1]
    else:
        return s[center_num]

print(solution(s_select))

