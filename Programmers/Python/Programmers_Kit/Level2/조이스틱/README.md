# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/42860

## Solving Point 
'A'가 연속으로 나오는 길이가 최대인 위치를 구한다.

Function :
    ord(Alp) -> Alphabet to ASCII
    chr(ASCII) -> ASCII to Alphabet 

'A'가 아닐 경우 'A'부터 바꾸는것과 거꾸로 바꾸는 것중 횟수 적은 것 선택

전체 탐색 끝난 후 
A 연속 시작점이 0  or 끝점이 문자열 끝일 경우:
    answer 에 문자열 길이 + 'A' 연속 길이 -1
나머지 : 
    비교 수행

    left = len(name) - a_end - 1
    if a_start <= left:
        move_cnt = (a_start-1)*2 + left
    else:
        move_cnt = (a_start-1) + 2*left
    answer += min(move_cnt ,len(name)-1)

### Time Complexity
O(N) : N: 문자열 길이