import random

# top line is 0
board = [[0] * 7 for _ in range(7)]
base = 0

# debug
def pboard():
    for i in range(7):
        for j in range(7):
            print(board[i][j], end=' ')
        print()

# clean line if full
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

# find adjacent seq
def find_seq_aux(p, dx, dy):
    seqs = []
    for i in range(7):
        for j in range(base, base + 7):
            s = []
            for k in range(4):
                x = j + k * dx
                y = i + k * dy
                if x < 7 and y < 7 and board[y][x] == p:
                    s.append((x, y))
                else:
                    break
            if k > 0:
                seqs.append(s)
    return seqs

def find_seq(p):
    seqs = find_seq_aux(p, 1, 0)        # horiziontals
    seqs.extend(find_seq_aux(p, 0, 1))  # verticals
    seqs.extend(find_seq_aux(p, 1, 1))  # diags
    seqs.extend(find_seq_aux(p, -1, 1)) # anti diags
    seqs.sort(key=lambda x: len(x))
    return seqs

def find_seq_max(p, length, dx, dy):
    for i in range(7):
        for j in range(base, base + 7):
            s = []
            for k in range(4):
                x = j + k * dx
                y = i + k * dy
                if x < 7 and y < 7 and board[y][x] == p:
                    s.append((x, y))
                else:
                    break
            if k > length:
                return True
    return False

def is_win(p, ptr):
    return find_seq_max(p, 4, 1, 0) or \
    find_seq_max(p, 4, 0, 1)  or \
    find_seq_max(p, 4, 1, 1)  or \
    find_seq_max(p, 4, -1, 1)  # anti

# STRATS
def move_random():
    return random.randint(0, 6)

# CHANGE STRAT
strat = move_random

# main loop
while(True):

    # opponent play
    move = int(input())

    if move >= 0:
        play(move, 2)
        if is_win(2, base):
            print("Perdu")
        clean()

    pboard()

    print("seq player 2")
    print(find_seq(2))

    # we play
    move = strat()
    play(move, 1)
    if is_win(1, base):
        print("Gagné")
    clean()

    print(move)
    pboard()
