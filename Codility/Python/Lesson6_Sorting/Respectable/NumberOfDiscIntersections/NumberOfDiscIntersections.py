# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    disc_list = []
    for i in range(len(A)) :
        disc_list.append([i-A[i],-1])
        disc_list.append([i+A[i],1])

    disc_list.sort()
    interval = 0
    intersect = 0
    for disc in disc_list:
        if disc[1] == 1:
            intersect -= 1
        else :
            interval += intersect
            intersect+=1

    return interval if interval <= 10000000 else -1