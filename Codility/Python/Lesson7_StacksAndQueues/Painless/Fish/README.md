# Problem URL
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

## Solving Point 

Stack 활용 문제
상류로 이동하는 물고기와, 하류로 이동하는 물고기 존재.
기준점 잡고(하류로 정함) 이동하는 물고기 stack에 넣음
반대 물고기의 경우 Stack 비교하며 잡아 먹힐 경우 Pop
Stack 비었을 경우 + 1 
마지막 stack 남은 물고기 + 살아 남은 물고기(?)

function:
     

### Time Complexity

O(N)