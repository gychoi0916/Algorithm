# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    answer = 0
    for i in range(len(A)) :
        if B[i] == 1:
            stack.append(A[i])
        else:
            while stack and stack[-1] < A[i] :
                stack.pop()
            if not stack:
                answer += 1

    return answer + len(stack) 