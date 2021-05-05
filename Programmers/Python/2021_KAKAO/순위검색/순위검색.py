from itertools import combinations


def solution(info, query):
    answer = []
    db = {}

    for inf in info:
        tmp = inf.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])

        for n in range(5):
            comb = combinations(range(4), n)

            for c in comb:
                tmp_condition = conditions.copy()

                for v in c:
                    tmp_condition[v] = '-'

                change_t_c = '/'.join(tmp_condition)

                if change_t_c in db:
                    db[change_t_c].append(score)
                else:
                    db[change_t_c] = [score]

    for value in db.values():
        value.sort()

    for q in query:
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])

        if qry_cnd in db:
            data = db[qry_cnd]

            if len(data) > 0:
                start, end = 0, len(data)

                while start != end and start != len(data):

                    if data[(start+end)//2] >= qry_score:
                        end = (start+end) // 2
                    else:
                        start = (start+end) // 2 + 1

                answer.append(len(data) - start)
        else:
            answer.append(0)

    return answer
