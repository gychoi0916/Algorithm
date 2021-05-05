# Problem URL

https://programmers.co.kr/learn/courses/30/lessons/42883

## Solving Point

Stack 활용
Stack의 Top 이 더 작으면 stock pop, K: 제거할 숫자 -1

Stack 비어있거나 Top보다 작으면 Stack에 추가

K != 0 :
stack = stack[:-k]

### Time Complexity

O(N)
