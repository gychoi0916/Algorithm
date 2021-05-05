# Problem URL

https://programmers.co.kr/learn/courses/30/lessons/72411

## Solving Point

libs, function :

    1) Combinations
        조합 경우의 수 combination 객체로 return
        from itertools import combinations
    2) Counter
        list 안의 원소들에 대한 개수 counter를 Dictionary ? 형태로 return

조건에 맞는 메뉴 조합 추가

if len(counter) != 0 and max(counter.values()) != 1:
answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

제한사항: counter 중 max인 경우 에만

### Time Complexity

O(NM) N: course 개수 M : 조합 개수,
