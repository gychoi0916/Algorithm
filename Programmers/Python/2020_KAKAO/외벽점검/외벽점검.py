from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1 # if no case
    weak_length = len(weak)
    
    for i in range(weak_length):
        weak.append(weak[i] + n)
    
    dist_perm = list(map(list,permutations(dist,len(dist))))
    
    for i in range(weak_length):
        start = [weak[j] for j in range(i,i+weak_length)]
        for dist_p in dist_perm:
            result = 1
            dist_distance = 0
            check_len = start[0] + dist_p[0]
            
            for k in  range(weak_length):
                if start[k] > check_len:
                    result += 1 
                    if result > len(dist_p):
                        break
                    dist_distance += 1
                    check_len = start[k] + dist_p[dist_distance]
            answer = min(answer,result)
    if answer > len(dist):
        return -1
    return answer 
#     weak_length = len(weak)
#     #distance X2 for direction problem
#     for i in range(weak_length):
#         weak.append(weak[i] + n)
#     #max input friend number for impossible + 1
#     answer = len(dist) + 1
#     for i in range(weak_length):
#         start_point = [weak[j] for j in range(i,i+ weak_length)]
#         candidates = permutations(dist,len(dist))
        
#         for order in candidates:
#             friend_idx, friend_cnt = 0, 1
#             possible_check_length = start_point[0] + order[friend_idx]
            
#             for idx in range(weak_length):
#                 if start_point[idx] > possible_check_length:
#                     friend_cnt += 1
#                     if friend_cnt > len(order):
#                         break
#                     friend_idx += 1
#                     possible_check_length = order[friend_idx] + start_point[idx]
#             answer = min(answer,friend_cnt)
#     if answer > len(dist):
#         return -1
#     return answer
        
#     return answer