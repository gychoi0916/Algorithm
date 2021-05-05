def solution(dirs):
    answer = 0
    dir_pair = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    dir_man = {"U": 0, "D": 1, "R": 2, "L": 3}
    visited = set()
    x, y = 0, 0

    for dir_c in dirs:
        tmp = dir_man[dir_c]
        next_x, next_y = dir_pair[tmp][0]+x, dir_pair[tmp][1] + y

        if next_x < -5 or next_x > 5 or next_y < -5 or next_y > 5:
            continue
        if (x, y, next_x, next_y) not in visited:
            visited.add((x, y, next_x, next_y))
            visited.add((next_x, next_y, x, y))
            answer += 1
        x, y = next_x, next_y

    return answer
