'''
20230701
[PGS] 제일 작은 수 제거하기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12935
'''

# 입출력 예
arr = [[4,3,2,1], [10]]
# return = [[4,3,2], [-1]]

sel_ex = 0
arr_select = arr[sel_ex]

def solution(arr):
    # 리스트에서 최소값을 찾은 뒤 리스트에서 삭제한다.
    arr.remove(min(arr))
    # 리스트 길이가 0보다 크면 arr 리스트를, 0이라면 [-1] 리스트를 리턴
    return arr if len(arr) > 0 else [-1]

print(solution(arr_select))
