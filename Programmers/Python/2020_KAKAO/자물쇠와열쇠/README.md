# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/60059

## Solving Point 

Algorithm : 
    1) 기존 열쇠 board에 key 크기 만큼 추가로 확장

    2) key를 끝부터 걸쳐 rotate, 이동 하며 확인
        => 2D array rotate 하는 법 확인

method, module :
    1) 2D Array Rotete
        list(zip(*key[::-1]))

### Time Complexity