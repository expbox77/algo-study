# [PGS] 소수 만들기 Lv.1

- 풀이 날짜: 20230707
- 출처: <https://school.programmers.co.kr/learn/courses/30/lessons/12977>

<br />

## 소수 만들기

### 문제 설명

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
- nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

### 입출력 예

| nums        | result |
| ----------- | ------ |
| [1,2,3,4]   | 1      |
| [1,2,7,6,4] | 4      |

### 입출력 예 설명

입출력 예 #1  
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2  
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.

<br />

## 공부할 개념

- 조합 `combinations()`
- 에라토스테네스의 체

<br />

## 문제 분석

**소수**라는 특성 때문에 이전의 [소수 찾기](/docs/%5BPGS%5D%EC%86%8C%EC%88%98%20%EC%B0%BE%EA%B8%B0-Lv.1.md) 문제가 떠올랐다. 이 문제에서 `에라토스테네스의 체`를 응용하면 어렵지 않게 풀이가 가능하다. 제한사항을 확인해보면 `3개의 숫자를 골라 더하는` 방식이며 `nums의 원소는 1이상 1,000 이하의 자연수`이기에 에라토스테네스의 체는 3,000을 넘지 않게 만들면 된다.

그 이후 nums에 있는 원소를 3개 골라야한다. 어짜피 합을 구해야하기에 **순열이 아닌 조합**이 되어야한다. 이 경우 직접 함수를 만들어도 상관없지만 파이썬 내장 함수 패키지인 `itertools`에서 `combinations` 함수를 불러와서 사용하면 된다. `combinations(list, n)`으로 사용하며 list에 조합으로 사용할 원소가 담긴 리스트를, n에는 몇 개의 원소를 고를지 입력하면된다. 다만 `combinations(list, n)`는 combinations 객체로 리턴이 되어 `list()` 함수를 사용해서 리스트화 시키는 것을 잊지 않아야한다.

<br />

## 나의 문제 풀이 코드

```python
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
```

앞선 에라토스테네스의 체는 [소수 찾기](/docs/%5BPGS%5D%EC%86%8C%EC%88%98%20%EC%B0%BE%EA%B8%B0-Lv.1.md)에서 설명을 했었기에 따로 설명하지 않는다.

`itertools` 패키지에서 `combinations` 함수를 불러와서 조합 리스트를 만든다. 그 조합 리스트를 불러와 합을 구하고 그 합이 에라토스테네스의 체에서 소수가 맞는지 확인하는 과정을 거친다. 만약 맞다면 `prime` 변수에 1을 더하여 소수가 되는 경우를 늘린다. 소수가되는 경우를 리턴해야한다면 `prime` 변수가 리스트가 되어 append 하면 될 것이라 생각한다.

<br />

## 다른 사람의 코드

```python
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])
```

이 풀이도 `combinations(nums,3)`를 사용하여 풀었다. 조합의 합을 `prime_number 함수`로 보내어 소수 판별을 한다. 하지만 이 경우 시간복잡도가 늘어날 수 있어 주의해야한다. 이론상 에라토스테네스의 체가 가장 시간복잡도가 가장 낮은 것을 고려해야한다.
