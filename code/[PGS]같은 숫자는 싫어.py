'''
20230614
[PGS] 같은 숫자는 싫어 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''

# 입출력 예
arr = [[1, 1, 3, 3, 0, 1, 1], [4, 4, 4, 3, 3]]
# answer = [[4, 4, 4, 3, 3], [4, 3]]
arr_select = arr[1]

# 1차 시도
# 합계: 100.0 / 100.0
def solution(arr):
    temp_list = [arr[0], ]
    for _ in arr:
        if _ != temp_list[-1]:
            temp_list.append(_)
    return temp_list

print(solution(arr_select))
