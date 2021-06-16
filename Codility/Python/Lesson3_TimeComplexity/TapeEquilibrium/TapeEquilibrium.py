# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 10000000

    left = 0
    right = sum(A)

    for i in range(len(A) - 1):
        left += A[i]
        right -= A[i]
        # print(left,right)
        if abs(left - right) < answer :
            answer = abs(left-right)
        
    return answer