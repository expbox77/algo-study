'''
20230618
[PGS] 문자열 내림차순으로 배치하기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12917
'''

# 입출력 예
s = ["Zbcdefg"]
# return = ["gfedcbZ"]

sel_ex = 0
s_select = s[sel_ex]

# 1차 시도
# 합계: 100.0 / 100.0
def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution(s_select))
