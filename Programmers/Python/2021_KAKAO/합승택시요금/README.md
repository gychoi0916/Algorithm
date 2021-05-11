# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/72413

## Solving Point 

Algorithm : 
    1) Dijkstra
    
    특정 지점에서 각 지점 까지 거리 최소 구하는 알고리즘. (priorityQueue(minheap) 사용)
    우선 시작 지점 넣고, distance 최대로 설정 후
    비교해보며 진행. next_node의 현재까지 distance + cost가 더 적으면 push

    2) 우선, start에서 a,b까지 각자 가는 것 구하고
    모든 node에 대해 같이 갔다가 찢어지는 것 구해서 최소 값을 답으로


method, module :
    1) minheap 사용
        import heapq

### Time Complexity
O(N * (E + VLogV)) => n * Dijkstra .. ?