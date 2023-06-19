'''
20000000
[PGS] 서울에서 김서방 찾기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12919

이전에 풀었던 문제로 관련 자료가 없이 그냥 풀어놓은 알고리즘 밖에 존재하지 않아 따로 리뷰는 하지 않음. 추후에 자료 발견 시 수정하겠음.

문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.
'''

# 입출력 예
seoul = [["Jane", "Kim"]]
#return = ["김서방은 1에 있다"]

sel_ex = 0
seoul_select = seoul[sel_ex]

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

print(solution(seoul_select))
