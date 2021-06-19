# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    start = 0
    answer = 0
    for i in range(len(A)) :
        if A[i] == 0 :
            start += 1
        else:
            answer += start
        
        if answer > 1000000000:
            return -1
    return answer