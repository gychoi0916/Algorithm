# Problem URL

https://programmers.co.kr/learn/courses/30/lessons/1844

## Solving Point

Algorithm :

    1) BFS :
        특정 지점에서 최단 거리 포인트 찾는 문제는
        BFS로 푸는 게 유리

method, module :

    1) deque
        collections module에 포함
        from collections import deque
        popleft, pop, append, appendleft, extend(left), rotate 등을 활용하여
        Queue, Stack 구조 형성하기에 용이 함
        pop/push 활발한 연산에서 list보다 유리

        cons : linked list의 형태로 (메모리 불연속) random access의 경우 불리

### Time Complexity
