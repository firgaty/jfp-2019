board = [[0] * 7 for _ in range(7)]

# 0 == nothing
# otherwise == player
def play(p, c):
    for i in range(7):
        if board[i][c] != 0:
            assert (i != 0)
            board[i - 1][c] = p

