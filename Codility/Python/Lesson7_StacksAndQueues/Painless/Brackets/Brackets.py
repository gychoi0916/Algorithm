# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    bracket_pair = {'}':'{',']':'[',')':'('}
    for s in S:
        if s in ['[','{','('] :
            stack.append(s)
        elif stack and stack[-1] == bracket_pair[s]:
            stack.pop()
        else:
            return 0

    if not stack:
        return 1
    return 0