'''
20230613
[PGS] 2016년 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12901
'''

a = 5
b = 24
# result = "TUE"


# 1차 시도
# 합계: 14.3 / 100.0
# 일부 오답이 있었음.
'''
def solution(a, b):

    import datetime as dt

    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return week[dt.datetime(2016, 5, 24, 0, 0).weekday()]
'''


# 2차 시도
# 합계: 100.0 / 100.0
def solution(a, b):

    import datetime as dt

    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return week[dt.datetime(2016, a, b).weekday()]


print(solution(a, b))