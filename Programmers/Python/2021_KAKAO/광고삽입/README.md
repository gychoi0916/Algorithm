# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/72414

## Solving Point 

Algorithm : 
    문자열 다루는 문제
    1) 전체 play time 에 재생 시작 time에 + 1 끝 time에 -1

    2) 한 번 순회 하며 time[i] = time[i] + time[i-1]
    => 몇 곡이 play 중인지

    3) 한 번 더
    => 가중치 구하기 위해 재생 구간 * (재생 중인 곡 수)


method, module :
    1) 문자열로 주어진 시간 -> 수치로, 반대  직접 define 

### Time Complexity
O(N)