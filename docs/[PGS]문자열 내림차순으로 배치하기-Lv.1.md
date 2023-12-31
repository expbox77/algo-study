# [PGS] 문자열 내림차순으로 배치하기 Lv.1

- 풀이 날짜: 20230618
- 출처: <https://school.programmers.co.kr/learn/courses/30/lessons/12917>

<br />

## 문자열 내림차순으로 배치하기

### 문제 설명

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.  
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

### 제한사항

- str은 길이 1 이상인 문자열입니다.

### 입출력 예

| s         | return    |
| --------- | --------- |
| "Zbcdefg" | "gfedcbZ" |

<br />

## 공부할 개념

- `join`
- `sorted(reverse=True)`을 사용한 내림차순 정렬

<br />

## 문제 분석

내림차순으로 정렬하는 방법은 그리 어렵지 않다. 기존의 `sorted()` 함수의 기본 값이 오름차순이라 이것을 내림차순으로 바꿔주는 방법은 `sorted()` 함수에서 `reverse` 값을 `True`로 맞춰주면 된다.

하지만 `sorted()` 함수는 **문자열이 자동으로 리스트로 변경된 후** 정렬된다. 처음에는 `map` 함수를 사용하여 리스트의 원소들을 문자열로 바꿔주려고 했으나 **map 객체 자체를 리턴하는 문제**가 있었다. 그래서 이 경우 `join`을 사용하여 리스트 내의 원소들을 문자열로 이어주어 문제를 해결했다.

<br />

## 나의 문제 풀이 코드

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

`sorted(reverse=True)`로 내림차순으로 정렬했으나 리스트로 값이 나오기 때문에 문자열로 변환되게끔 해주는 과정이 필요하다. 따라서 `''.join()`을 사용하여 각 원소의 사이에 넣을 문자를 없게 만들어주어 리스트가 문자열로 변환되게 하였다.

<br />

## 다른 사람의 코드

```python
def solution(s):
    return ''.join(sorted(s, reverse=True))
```

신기하게도 나와 글자 하나 틀리지 않은 코드를 사용한 사람들이 많았다.
