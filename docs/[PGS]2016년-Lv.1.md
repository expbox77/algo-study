# [PGS] 2016년 Lv.1

- 풀이 날짜: 20230613
- 출처: <https://school.programmers.co.kr/learn/courses/30/lessons/12901>

<br />

## 2016년

### 문제 설명

2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 `SUN,MON,TUE,WED,THU,FRI,SAT` 입니다.

예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

### 제한사항

- 2016년은 윤년입니다.
- 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

### 입출력 예

| a   | b   | result |
| --- | --- | ------ |
| 5   | 24  | "TUE"  |

<br />

## 공부할 개념

- [`datetime 패키지`](https://docs.python.org/ko/3/library/datetime.html#datetime-objects)

<br />

## 문제 분석

2016년은 윤년으로 1월부터 12월까지 각각의 날짜가 `31,29,31,30,31,30,31,31,30,31,30,31`일이다. 나는 이 날짜를 각각 다 더하고 빼는 등의 계산을 하는것보다 파이썬에 기본적으로 탑재되어있는 패키지인 `datetime`을 사용하는 것이 더 좋은 방법이라 생각했다. 실제로 내가 강의를 들었던 코딩테스트 강의에서 강사님께서 자신도 자체적인 라이브러리를 구축하려고 했는데 어떻게 해봐도 오픈소스(에 기여한 사람들)와 다양한 석/박사들이 만들어놓은 알고리즘보다 더 빠르게 실행되지 않았다고 이야기했다. 다른 프로그래밍 언어에서는 직접 구축해야하겠지만 파이썬은 그럴 필요가 크게 없다는 뜻으로 해석했다.

따라서 `datetime` 패키지를 사용하여 어떤 날짜에 어떤 요일이 어떻게 표현되는지 확인해봤다. 그랬더니 월요일 ~ 일요일 순으로 0번부터 6번까지로 표현되는 것으로 [확인](https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html#id2)했다. 이것을 바탕으로 알고리즘을 완성했다.

<br />

## 나의 문제 풀이 코드

```python
# 1차 시도
def solution(a, b):
    import datetime as dt
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return week[dt.datetime(2016, 5, 24, 0, 0).weekday()]
```

<br />

1차 시도에는 바보같이 입출력 예에 사용했던 그대로를 리턴값으로 넣어주는 바람에 오답이 나와버렸다. 전에 했던 [\[PGS\]폰켓몬](/docs/[PGS]폰켓몬-Lv.1.md)에서도 이런 실수를 했는데 실제 제출할 때는 오답이라고 나오지도 않고 제출하면 끝이니 이런 실수를 최대한 줄여야겠다고 생각했다.

```python
# 2차 시도
def solution(a, b):
    import datetime as dt
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return week[dt.datetime(2016, a, b).weekday()]
```

리턴에서 datetime 부분을 `dt.datetime(2016, a, b)`로 바꿔주었고 정상적으로 정답 처리가 되었다.

<br />

## 다른 사람의 코드

```python
def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    stack_day = sum(month[:a-1])+b
    answer= day[stack_day%7]
    return answer
```

원래 문제 출제자의 의도는 이게 아니었을까 싶다. `2016년 1월 1일`이 금요일이니 day 리스트에서 1번 자리에 오게끔 리스트를 만들고 각 달마다의 날짜를 리스트로 만든다. 그리고는 stack_day에서 mounth 리스트를 슬라이싱하여 모든 날을 더한다. 그리고는 모든 날을 더한 값에서 7을 나눈 나머지가 무슨 요일인지 알려주는 숫자이기 떄문에 day 리스트에서 그에 맞는 요일을 출력하게 만든다.
