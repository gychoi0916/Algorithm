# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    visited = set()

    for i in range(len(A)):
        visited.add(A[i])

        if len(visited) == X :
            return i

    return -1