# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    answer = 0 
    stack = []

    for h in H:
        while stack and stack[-1] > h :
            stack.pop()
        if not stack or stack[-1] < h :
            stack.append(h)
            answer += 1

    return answer