def solution(p):
    # answer = ''
    # answer = parentheses(p)
    # 1. void str
    if len(p) == 0:
        return ''
    # 2. split u,v
    flag = 0
    for i in range(len(p)):
        if p[i] == '(':
            flag += 1 
        else:
            flag -= 1
        if flag == 0:
            u = p[0:i+1]
            if i+1 <= len(p) - 1:
                v = p[i+1:]
            else:
                v = ''
            break
    if u[0] == '(':
        return u + solution(v)
    else:
        tmp = ''
        for i in range(1,len(u)-1):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('
        return '('+solution(v)+ ')' + tmp