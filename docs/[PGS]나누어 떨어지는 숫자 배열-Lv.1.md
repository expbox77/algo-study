# [PGS] 나누어 떨어지는 숫자 배열 Lv.1

- 풀이 날짜: 20230615
- 출처: <https://school.programmers.co.kr/learn/courses/30/lessons/12910>

<br />

## 나누어 떨어지는 숫자 배열

### 문제 설명

array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.

divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

### 제한사항

- arr은 자연수를 담은 배열입니다.
- 정수 $i, j$에 대해 $i \neq j$ 이면 $arr[i] \neq arr[j]$ 입니다.
- divisor는 자연수입니다.
- array는 길이 1 이상인 배열입니다.

### 입출력 예

| arr           | divisor | return        |
| ------------- | ------- | ------------- |
| [5, 9, 7, 10] | 5       | [5, 10]       |
| [2, 36, 1, 3] | 1       | [1, 2, 3, 36] |
| [3,2,6]       | 10      | [-1]          |

### 입출력 예 설명

입출력 예#1  
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

입출력 예#2  
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

입출력 예#3  
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

<br />

## 공부할 개념

- `sorted()`
- if / for 문의 한줄 코딩

<br />

## 문제 분석

문제를 보자마자 이전에 풀었던 [같은 숫자는 싫어](/docs/%5BPGS%5D%EA%B0%99%EC%9D%80%20%EC%88%AB%EC%9E%90%EB%8A%94%20%EC%8B%AB%EC%96%B4.md) 문제가 생각났다. 중복 제거로 사용했던 알고리즘을 이번에는 divisor로 나누었을 때 나머지가 없다면 임시 리스트에 추가, 아니라면 추가하지 않도록한다. 그리고 중요한 것이 바로 리스트를 `오름차순`으로 정렬하는 것이다. 오름차순은 `sorted()` 함수를 사용하여 정렬이 가능하다. 만약 `내림차순`으로 지정해야하면 `sorted(list1, reverse=True)`로 reverse 매개 변수를 **True**로 만들면 된다.

하지만 이렇게 간단하게 문제를 풀고 넘어가는 것은 그리 좋지 않다고 생각했다. 그래서 이전에 조금 사용해봤던 if문과 for문을 한줄로 코딩하는 방법을 사용하여 처음 짰던 코드를 조금 더 단순하게 만들어보는 작업을 추가로 했다.

<br />

## 나의 문제 풀이 코드

```python
# 처음 작성한 코드
def solution(arr, divisor):
    temp_arr = []
    for _ in arr:
        if _ % divisor == 0:
            temp_arr.append(_)
    if len(temp_arr) == 0:
        return [-1]
    else:
        return sorted(temp_arr)
```

temp_arr를 만들었다. 그리고 arr의 원소를 하나씩 가져와서 divisor의 값과 나눈 나머지가 없다면 temp_arr에 가져왔던 arr의 원소를 추가한다. 만약 temp_arr에 아무 원소도 존재하지 않는다면 [-1]을 출력하라고 했으니 temp_arr의 길이가 0이라면 [-1]을 리턴하게 된다. temp_arr의 길이가 1이상이라면 `sorted()` 함수를 사용하여 오름차순으로 정렬한 값을 리턴한다.

<br />

```python
# 한줄 코딩으로 수정
def solution2(arr, divisor):
    temp_arr = [num for num in arr if num % divisor == 0]
    return [-1] if len(temp_arr) == 0 else sorted(temp_arr)
```

한줄 코딩은 [이 블로그](https://stcodelab.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%93%B0%EA%B8%B0)의 글을 참고했다. temp_arr 리스트를 생성하면서 처음부터 위에 처음 작성한 코드의 for 문을 실행하도록 했다. 그리고 리턴을 줄때 if - else 문을 한줄 코딩해봤다. 코드 자체는 줄어든 것 같은데 익숙해지기 전 까지는 이해하는데 어려울 것 같다. 다른 문제를 풀면서 조금 더 익숙해져야겠다.

<br />

## 다른 사람의 코드

```python
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
```

뭔가 좀 더 줄일 수 있지 않을까 생각해서 temp_arr를 빼려는 시도를 좀 했는데 역시 실력자는 많은 것 같다. `or`을 사용하는 것인데 댓글을 좀 보니 **빈 리스트**는 `False`로 작동한다는 것을 새롭게 알게 되었다. 이렇게 되면 `if 문`을 `or`가 대체하게 되니 생각치도 못한 활용방법인 것 같다.
