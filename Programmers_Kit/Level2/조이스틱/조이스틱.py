def solution(name):
    answer = 0
    a_max = 0
    a_start = 0
    a_end = 0
    a_cnt = 0
    
    for i in range(len(name)):
        if name[i] == 'A':
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                a_end = i
        else:
            answer += min(ord(name[i]) - ord('A'),ord('Z') - ord(name[i])+1)
            a_cnt = 0
        
    a_start = a_end - a_max + 1
    
    if a_start == 0 or a_end == len(name) -1:
        answer+= len(name) - a_max + 1
    else:
        left = len(name) - a_end - 1
        if a_start <= left:
            move_cnt = (a_start-1)*2 + left
        else:
            move_cnt = (a_start-1) + 2*left
        answer += min(move_cnt ,len(name)-1)

    return answer 