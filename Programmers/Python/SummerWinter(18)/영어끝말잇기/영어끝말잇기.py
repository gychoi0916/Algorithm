def solution(n, words):
    answer = []
    tmp = set()
    end = ""
    start = ""

    for i in range(len(words)):
        start = words[i][0]

        if i > 0:
            if start != end:
                # print(start,end)
                if (i+1) % n == 0:
                    return [n, (i+1) // n]
                else:
                    return[(i+1) % n, ((i+1) // n) + 1]

        before = len(tmp)
        tmp.add(words[i])
        after = len(tmp)

        if after == before:
            break

        end = words[i][-1]

    else:
        return [0, 0]

    if (i+1) % n == 0:
        return [n, (i+1) // n]

    else:
        return[(i+1) % n, ((i+1) // n) + 1]

    return answer

    # 다른사람 풀이
    #  for p in range(1, len(words)):
    #     if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    # else:
    #     return [0,0]
