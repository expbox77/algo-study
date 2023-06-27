'''
20230627
[PGS] 수박수박수박수박수박수? Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12922
'''

# 입출력 예
n = [3, 4]
# answer = ["수박수", "수박수박"]

sel_ex = 0
n_select = n[0]

def solution(n):
    return "수박" * int(n / 2) if n % 2 == 0 else "수박" * int(n / 2) + "수"

print(solution(n_select))
