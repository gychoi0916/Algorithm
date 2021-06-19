# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    peaks = []
    for i in range(1,len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)

    if not peaks:
        return 0

    for i in range(len(A)//2,0,-1):
        tmp = 0 
        if len(A) % i != 0 :
            continue
        if i > len(peaks):
            continue
        for peak in peaks:
             start = tmp * (len(A) // i )
             end = (tmp+1)*(len(A) // i )
             if peak >= start and peak < end:
                 tmp+= 1
        if tmp == i :
            return i