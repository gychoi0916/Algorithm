# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/42746

## Solving Point 

문자열로 변형하여 사전 순으로 정렬하는데,
3, 30의 경우 303 보다 330이 우선 순위 이기 때문에 이와 같은 경우,
1000이하라는 제한사항 덕에 문자열 * 3으로 사전 역순 정렬

for문 직접 구현 방법 외에
function:
    map() 함수 이용 가능

numbers = list(map(str, numbers))

### Time Complexity
O(NlogN) : sort 시간