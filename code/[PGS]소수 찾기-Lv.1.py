'''
20230625
[PGS] 소수 찾기 Lv.1
https://school.programmers.co.kr/learn/courses/30/lessons/12921
'''

# 입출력 예
n = [10, 5]
#result = [4, 3]

sel_ex = 0
n_select = n[sel_ex]

# 에라토스테네스의 체를 활용한 코딩
# 합계: 100.0 / 100.0
# 참고1: https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%86%8C%EC%88%98%EC%B0%BE%EA%B8%B0-Python
# 참고2: https://codingpractices.tistory.com/entry/Python-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

def solution(n):
    temp = [False, False,] + [True] * (n - 1)
    prime = 0

    for i in range(2, n + 1):
        if temp[i]:
            # temp 리스트에서 True값을 가진 인덱스가 소수이니까 바로 prime 변수에 1을 더해서 len()하는 시간까지도 아낄 수 있도록.
            prime += 1
            for j in range(2 * i, n + 1, i):
                temp[j] = False

    return prime

print(solution(n_select))
