# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)

    min_avg = (A[0] + A[1]) / 2
    result = 0
    if N == 2 :
        return result 

    for i in range(N-1) :
        avg2 = (A[i]+A[i+1]) / 2

        if avg2 < min_avg :
            result = i 
            min_avg = avg2
        
        if i < N-2:
            avg3 = (A[i]+A[i+1]+A[i+2]) / 3

            if avg3 < min_avg:
                result = i
                min_avg = avg3
    
    return result