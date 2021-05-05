# Problem URL

https://programmers.co.kr/learn/courses/30/lessons/72412

## Solving Point

Algorithm :

    문자열을 다루고, Combination을 활용해
    모든 경우의 수를 미리 만들어 놓음
    '-'가 각 컨디션 마다 존재할 경우 생성
    이후 효율성 문제로 점수로 정렬하여 이분 탐색 진행.

method, module :

    1) combinations:
        from itertools import combinations

    2) string method:
        split() : 문자열을 특정 문자로 분리 (없을 시 공백으로)
        (str).join(list) : list의 원소들을 str로 붙여서 이음.

    3) (dict).values() :
        dictionary의 key 별 value들을 반환 ?

### Time Complexity
