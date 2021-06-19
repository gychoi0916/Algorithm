# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # max_sum = A[0]
    max_tmp = A[0]
    answer = A[0]

    for i in range(1,len(A)):
        max_tmp = max(A[i],max_tmp + A[i])
        if answer < max_tmp:
            answer = max_tmp

    return answer