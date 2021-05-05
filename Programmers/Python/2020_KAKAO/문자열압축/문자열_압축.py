def solution(s):
    answer = len(s)
    ans_str = ''
    for i in range(1,len(s) // 2 + 1):
        cnt = 1
        tmp = s[0:i]
        for j in range(i,len(s),i):
            cmp = s[j:j+i]
            if cmp == tmp :
                cnt += 1 
            else:
                if cnt == 1:
                    ans_str += tmp
                else:
                    ans_str = ans_str + str(cnt) + tmp
                    cnt = 1
                tmp = cmp
                
            if j+i >= len(s):
                if cnt != 1:
                    ans_str = ans_str + str(cnt) + tmp
                    cnt = 1
                    break
                else:
                    ans_str += s[j:]
        if cnt != 1 :
            ans_str = ans_str + str(cnt) + tmp

        if len(ans_str) < answer :         
            answer = len(ans_str)
        ans_str = ''       
    return answer