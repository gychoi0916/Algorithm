# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    num_dict = {}
    dom = 0
    # dom_num = 0
    left_num = 0
    right_num = 0
    answer = 0

    for a in A:
        if a in num_dict:
            num_dict[a] += 1
        else:
            num_dict[a] = 1

    for num in num_dict:
        if num_dict[num] > len(A) // 2:
            right_num = num_dict[num]
            dom= num
            break

    for i in range(len(A)):
        if A[i] == dom:
            right_num -= 1
            left_num += 1
        if left_num > (i+1) // 2 and right_num > (len(A)-i-1) // 2:
            answer += 1
    
    return answer