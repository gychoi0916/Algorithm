# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if len(A) <= 1:
        return 0
        
    min_price = A[0]
    max_tmp = 0
    answer = 0

    for i in range(1,len(A)):
        max_tmp = A[i] - min_price
        if A[i] < min_price:
            min_price = A[i]

        if answer < max_tmp:
            answer = max_tmp

    if answer <= 0:
        return 0
    return answer