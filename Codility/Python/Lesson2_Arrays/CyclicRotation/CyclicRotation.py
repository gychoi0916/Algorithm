# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    if N == 0 : 
        return []
    if K >= N:
        K = K % N
    
    result = A[-K:] + A[: -K]

    return result
    # pass