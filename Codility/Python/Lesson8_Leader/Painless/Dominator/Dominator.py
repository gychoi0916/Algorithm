# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num_dict = {}

    for a in A:
        if a in num_dict:
            num_dict[a] += 1
        else:
            num_dict[a] = 1

    for num in num_dict:
        if num_dict[num] > len(A) // 2:
            return A.index(num)

    return -1