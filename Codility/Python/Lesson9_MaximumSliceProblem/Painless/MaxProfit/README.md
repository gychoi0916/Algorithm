# Problem URL
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/

## Solving Point 

카데인 알고리즘!!!
초기에 Sort 진행 후 구하려 했으나, O(NlogN) 및 전체 케이스 검사 시 O(N^2)
DP 알고리즘 일종인 카데인 알고리즘 참고하여 진행
A[i]에서 가질 수 있는 최소 값은 A[0]~A[i-1] 중에 존재 탐색하며 계산 가능
O(N) 해결

function:
     

### Time Complexity

O(N) 