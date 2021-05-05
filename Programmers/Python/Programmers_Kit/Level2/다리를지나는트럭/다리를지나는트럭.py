def solution(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    cur_bridge = [0] * bridge_length
    answer = 1
    cur_weight = truck_weights.pop()
    cur_bridge[bridge_length-1] = cur_weight

    while len(cur_bridge) > 0:
        cur_weight -= cur_bridge.pop(0)

        if truck_weights and truck_weights[len(truck_weights)-1] + cur_weight <= weight:
            tmp = truck_weights.pop()
            cur_bridge.append(tmp)
            cur_weight += tmp
        elif len(truck_weights) > 0:
            cur_bridge.append(0)

        answer += 1

    return answer
