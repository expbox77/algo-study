'''
20230619
[PGS] 문자열 다루기 기본 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12918
'''

# 입출력 예
s = ["a234", "1234", "12321234"]
# return = [false, true]

sel_ex = 2
s_select = s[sel_ex]

# 1차 시도
# 합계: 73.3 / 100.0
'''
def solution(s):
    if len(s) % 4 == 0 or len(s) % 6 == 0:
        return s.isdigit()
'''

# 2차 시도
# 합계: 96.7 / 100.0
'''
def solution(s):
    if len(s) % 4 == 0 or len(s) % 6 == 0:
        return s.isdigit()
    else:
        return False
'''

# 3차 시도
# 합계: 100.0 / 100.0
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False

print(solution(s_select))
