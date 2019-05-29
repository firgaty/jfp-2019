# top line is 0
board = [[0] * 7 for _ in range(7)]

# 0 == nothing
# otherwise == player
def play(p, c):
    for i in range(7):
        if board[i][c] != 0:
            assert (i != 0)
            board[i - 1][c] = p

def cp_move():
    return 0

while(True):

    move = int(input())

    if move < 0:
        play(3, 1)
        continue

    play(move, 2)

    move = cp_move()
    play(move, 1)

    print(move)
