# Problem URL
https://programmers.co.kr/learn/courses/30/lessons/60062

## Solving Point 

Algorithm : 
    1) 원 모양의 외벽을 길게 늘여 직선으로 표현
    => len(weak) 만큼 list 추가
    
    2) distance(움직일 수 있는 거리)를 permutation 수행 하여 순서 mix

    3) 취약 지점 for 문을 돌며 permutation을 돌고 length 비교 .


method, module :
    1) permutation 객체 list로 변환
        dist_perm = list(map(list,permutations(dist,len(dist))))

### Time Complexity