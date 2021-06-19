# Problem URL
https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/

## Solving Point 

maxSliceSum 변형 문제.
왼쪽 오른쪽 별로 부분 maxSliceSum 구해 놓고 0, len(A) -1 제외(범위 주의)
다시 한 번 탐색하며 중간 P 부분 제외 최대 합 구한다.

function:
     

### Time Complexity

O(N) 