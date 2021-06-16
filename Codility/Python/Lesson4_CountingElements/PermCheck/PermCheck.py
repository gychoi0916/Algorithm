# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    if len(set(A)) == len(A) and sum(A) == sum(range(len(A)+1)):
        return 1
    return 0