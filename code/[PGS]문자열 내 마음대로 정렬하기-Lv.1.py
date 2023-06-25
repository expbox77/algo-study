'''
20230625
[PGS] 문자열 내 마음대로 정렬하기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12915
'''

# 입출력 예
strings = [["sun", "bed", "car"], ["abce", "abcd", "cdx"]]
n = [1, 2]
# return = [["car", "bed", "sun"], ["abcd", "abce", "cdx"]]

sel_ex = 1
strings_select = strings[sel_ex]
n_select = n[sel_ex]


# 1차 시도
# 합계: 16.7 / 100.0
'''
def solution(strings, n):
    return sorted(strings, key = lambda x : x[n])
'''

# 2차 시
# 합계: 100.0 / 100.0
# 참고: https://velog.io/@jerry_bak/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%A7%88%EC%9D%8C%EB%8C%80%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-python
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x : x[n])

print(solution(strings_select, n_select))
