def rotate(key):
    return list(zip(*key[::-1]))


def insert(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[i+x][j+y] += key[i][j]


def extract(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[i+x][j+y] -= key[i][j]


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]

    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                insert(x, y, M, key, board)
                if check(board, M, N):
                    return True
                extract(x, y, M, key, board)

    return False
# def rotation(key):
#     array = [[0] * len(key) for i in range(len(key))]

#     for i in range(len(key)):
#         for j in range(len(key)):
#             array[j][len(key)-1-i] = key[i][j]

#     return array


# def check(row, col, key, lock, ex_lock, start, end):
#     check_mat = [[0]*ex_lock for i in range(ex_lock)]
#     for i in range(len(key)):
#         for j in range(len(key)):
#             check_mat[row + i][col + j] += key[i][j]

#     for i in range(start, end):
#         for j in range(start, end):
#             check_mat[i][j] += lock[i - start][j-start]

#             if check_mat[i][j] != 1:
#                 return False
#     return True


# def solution(key, lock):
#     start = len(key) - 1
#     end = len(key) + len(lock) - 1
#     ex_lock = len(lock) + start * 2

#     for rot in range(4):
#         for row in range(end):
#             for col in range(end):
#                 if check(row, col, key, lock, ex_lock, start, end):
#                     return True
#         key = rotation(key)

#     return False
