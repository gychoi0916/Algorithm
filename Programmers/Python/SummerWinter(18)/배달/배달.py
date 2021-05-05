# Dijkstra Algorithm
from queue import PriorityQueue


def dijkstra(road, N):
    dist = [5000001] * (N+1)
    dist[1] = 0
    pq = PriorityQueue()
    pq.put([0, 1])

    while not pq.empty():
        cost, here = pq.get()

        if cost > dist[here]:
            continue

        for i in range(len(road)):

            if road[i][0] == here:
                cost2, next_p = road[i][2] + cost, road[i][1]

                if cost2 < dist[next_p]:
                    dist[next_p] = cost2
                    pq.put([cost2, next_p])

            elif road[i][1] == here:
                cost2, next_p = road[i][2] + cost, road[i][0]

                if cost2 < dist[next_p]:
                    dist[next_p] = cost2
                    pq.put([cost2, next_p])

    return dist


def solution(N, road, K):
    answer = 0
    dist = dijkstra(road, N)

    for i in dist:
        if i <= K:
            answer += 1

    return answer
