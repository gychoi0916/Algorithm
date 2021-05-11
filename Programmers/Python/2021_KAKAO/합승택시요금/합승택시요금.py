import heapq


def dijkstra(graph, start, destination):
    INF = int(1e9)
    distance = [INF for _ in range(len(graph))]
    # print(distance)
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        # print(heap)
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for cost, next_point in graph[now]:
            next_dist = cost + dist
            if distance[next_point] > next_dist:
                distance[next_point] = next_dist
                heapq.heappush(heap, [next_dist, next_point])

    return distance[destination]


def solution(n, s, a, b, fares):
    graph = [[]for _ in range(n+1)]
    for p1, p2, fare in fares:
        graph[p1].append([fare, p2])
        graph[p2].append([fare, p1])
    # print(graph)
    answer = dijkstra(graph, s, a) + dijkstra(graph, s, b)
    for i in range(1, n + 1):
        if i != s:
            answer = min(answer, dijkstra(graph, s, i) +
                         dijkstra(graph, i, a) + dijkstra(graph, i, b))
    return answer
