# Problem URL
https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

## Solving Point 

Prefix Sum 알고리즘 활용 문제 !
처음 생각한 방식은 O(N*M)으로 퍼포먼스 문제.
Counter (유전 정보 추가 됨에 따라 count되는 list) 활용하여 풀이.
미리 계산 해놓고
Query에 따라 비교하며 계산.

function:
    

### Time Complexity
O(N*M) => O(N+M)    