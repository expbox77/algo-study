'''
20230707
[PGS] 소수 만들기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''

# 입출력 예
nums = [[1,2,3,4], [1,2,7,6,4]]
# result = [1, 4]

sel_ex = 1
nums_select = nums[sel_ex]

def solution(nums):
    # 에라토스테네스의 체
    temp = [False, False,] + [True] * (3000 - 1)
    prime = 0
    n = 3000

    # nums의 각 원소는 1 이상 1,000 이하의 자연수라서 3개 조합하면 대충 최대 3,000까지 에라토스테네스의 체를 만들어놓으면 된다.
    for i in range(2, n + 1):
        if temp[i]:
            for j in range(2 * i, n + 1, i):
                temp[j] = False

    # 조합
    from itertools import combinations

    combi_list = list(combinations(nums, 3))

    for _ in combi_list:
        if temp[sum(_)] == True:
            prime += 1

    return prime

print(solution(nums_select))
