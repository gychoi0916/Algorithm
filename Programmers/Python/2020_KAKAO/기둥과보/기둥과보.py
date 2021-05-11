def check(result):
    for x, y, a in result:
        # 기둥
        if a == 0:
            if y == 0:
                continue
            if [x-1, y, 1] in result or [x, y-1, 0] in result or [x, y, 1] in result:
                continue
            else:
                return False
        else:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = []
    for x, y, a, b in build_frame:
        if b == 1:
            result.append([x, y, a])
            valid = check(result)
            if valid == False:
                result.remove([x, y, a])
        else:
            result.remove([x, y, a])
            valid = check(result)
            if valid == False:
                result.append([x, y, a])
    result.sort()
    print(result)
    return result
