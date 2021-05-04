import heapq
def solution(scoville, K):
    answer = 0
    scov_heap = []
    for sco in scoville:
        heapq.heappush(scov_heap,sco)
    
    while scov_heap[0] < K:
        if len(scov_heap) == 1:
            return -1
        tmp1 = heapq.heappop(scov_heap)
        tmp2 = heapq.heappop(scov_heap)
        heapq.heappush(scov_heap,tmp1+tmp2*2)
        answer += 1
    return answer