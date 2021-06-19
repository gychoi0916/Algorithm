# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    left_sum = [0] * len(A)
    right_sum = [0] * len(A)

    if len(A) == 3:
        return 0

    for i in range(1, len(A)-1):
        left_sum[i] = max(left_sum[i-1]+A[i] , 0)
        right_sum[len(A) - i - 1] = max(right_sum[len(A) - i]+ A[len(A)-i -1],0)


    answer = 0

    for i in range(1,len(A)-1):
        answer = max(answer,left_sum[i-1]+right_sum[i+1])

    return answer