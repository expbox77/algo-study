'''
20230615
[PGS] 나누어 떨어지는 숫자 배열 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12910
'''

# 입출력 예
arr = [[5, 9, 7, 10], [2, 36, 1, 3], [3,2,6]]
divisor = [5, 1, 10]
# return = [[5, 10], [1, 2, 3, 36], [-1]]

arr_select = arr[2]
divisor_select = divisor[2]

# 최초 코딩
def solution(arr, divisor):
    temp_arr = []
    for _ in arr:
        if _ % divisor == 0:
            temp_arr.append(_)
    if len(temp_arr) == 0:
        return [-1]
    else:
        return sorted(temp_arr)
    
# 한줄 코딩으로 수정
def solution2(arr, divisor):
    temp_arr = [num for num in arr if num % divisor == 0]
    return [-1] if len(temp_arr) == 0 else sorted(temp_arr)
    
print(solution(arr_select, divisor_select))
print(solution2(arr_select, divisor_select))
