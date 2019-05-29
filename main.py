import random

# top line is 0
board = [[0] * 7 for _ in range(7)]

def is_tetris():
    for e in board[6]:
        if e == 0:
            return False
    return True

def clean():
    if is_tetris():
        board.pop()
        board.insert(0, [0] * 7)

# 0 == nothing
# otherwise == player
def play(c, p):
    for i in range(7):
        if board[i][c] != 0:
            assert (i != 0)
            board[i - 1][c] = p
            return

    board[6][c] = p

def cp_move():
    return random.randint(0, 6)

def pboard():
    for i in range(7):
        for j in range(7):
            print(board[i][j], end=' ')
        print()


while(True):

    # opponent play
    move = int(input())

    if move >= 0:
        play(move, 2)
        clean()

    pboard()

    # we play
    move = cp_move()
    play(move, 1)
    clean()

    print(move)
    pboard()
