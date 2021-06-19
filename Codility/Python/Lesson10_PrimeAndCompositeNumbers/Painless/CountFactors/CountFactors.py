# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math
def solution(N):
    # write your code in Python 3.6
    answer = 0

    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            answer += 2 

    if math.pow(int(math.sqrt(N)),2) == N:
        answer -= 1 

    return answer 