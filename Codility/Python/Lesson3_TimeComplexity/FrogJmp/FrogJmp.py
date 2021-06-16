# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    if X >= Y:
        return 0

    rest = Y - X

    if rest % D == 0:
        return rest // D
    else :
        return rest // D + 1