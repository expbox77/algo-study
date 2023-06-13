'''
20230613
[PGS] 폰켓몬 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''

# 입출력 예
nums = [[3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]]
# result = [2, 3, 2]

# 입출력 예 1
nums_select = nums[1]

# 1차 시도
# 합계: 70.0 / 100.0
# 일부 틀린 답이 나오는 경우가 있었음.
'''
def solution(nums):
    if len(nums) / 2 >= len(set(nums)):
        return len(set(nums))
    else:
        return len(nums)
'''

# 2차 시도
# 합계: 100.0 / 100.0
def solution(nums):
    if len(nums) / 2 >= len(set(nums)):
        return len(set(nums))
    else:
        return int(len(nums) / 2)

print(solution(nums_select))



