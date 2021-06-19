# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

######### 이전 코드 #######
# def solution(S, P, Q):
#     # write your code in Python 3.6
#     dna_dict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
#     tmp = []
#     result = []
#     for i in range(len(P)):
#         tmp = list(set(list(S[P[i]:Q[i]+1])))
        
#         answer = 5

#         for i in tmp:
#             if dna_dict[i] < answer:
#                 answer = dna_dict[i]
#         result.append(answer)

#     return result

def solution(S, P, Q):
    # write your code in Python 3.6
    M = len(P)
    A =[[0,0,0,0]]

    counter = [0] * 4
    result = []

    for i in S:
        if i == 'A':
            counter[0] += 1
            A.append(counter[:])
        elif i =='C':
            counter[1] += 1
            A.append(counter[:])
        elif i =='G':
            counter[2] += 1
            A.append(counter[:])
        elif i =='T':
            counter[3] += 1
            A.append(counter[:])
    
    for i in range(M):
        for j in range(4):
            val = A[Q[i]+1][j] - A[P[i]][j]
            if val != 0:
                result.append(j+1)
                break

    return result