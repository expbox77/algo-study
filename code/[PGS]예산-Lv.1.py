'''
20230707
[PGS] 예산 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12982

3시간 초과
'''

# 입출력 예
d = [[1, 3, 2, 5, 4], [2, 2, 3, 3]]
budget = [9, 10]
# result = [3, 4]

sel_ex = 0
d_select = d[sel_ex]
budget_select = budget[sel_ex]

# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

def solution(d, budget):
    sd = sorted(d)
    answer = 0
    sum = 0
    for i in sd :
        sum += i
        if sum > budget :
            break
        answer += 1
    return answer

print(solution(d_select, budget_select))
