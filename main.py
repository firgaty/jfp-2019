import random

# top line is 0
board = [[0] * 7 for _ in range(100)]
base = 0

L = 6
C = 7

# debug
def pboard():
    for i in range(L):
        for j in range(C):
            print(board[base + L - i - 1][j], end=' ')
        print()

# clean line if full
def is_tetris():
    for e in board[base]:
        if e == 0:
            return False
    return True

def clean():
    global base
    if is_tetris():
        base += 1
        return True
    return False

# 0 == nothing
# otherwise == player
def play(c, p):
    for i in range(L):
        if board[base + L - i - 1][c] != 0:
            assert (i != 0)
            board[base + L - i][c] = p
            return base + L - i

    board[base][c] = p
    return base

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
    for i in range(base, base + L):
        for j in range(C):
            s = []
            for k in range(4):
                x = j + k * dx
                y = i + k * dy
                if x < 7 and y < 7 and board[y][x] == p:
                    s.append((x, y))
                else:
                    break
            if len(s) >= 4:
                return True
    return False

def is_win(p, ptr):
    return find_seq_max(p, 4, 1, 0) or \
    find_seq_max(p, 4, 0, 1)  or \
    find_seq_max(p, 4, 1, 1)  or \
    find_seq_max(p, 4, -1, 1)  # anti

# STRATS
# 1  me
# -1 opp
def stockfish(depth, p):
    scores = [0] * 7

    if depth == 0:
        # calcul
        return scores

    for c in range(7):
        i = play(p + 1, c)
        # test is win
        scores[c] = stockfish(p * (-1))
        board[i][c] = 0

    return max(scores) / 2

def move_stockfish():
    scores = stockfish(10)
    c, m = 0, scores[0]
    for i in range(1, 7):
        if scores[i] > m:
            c, m = i, scores[i]

    return c

def move_random():
    pos = []
    for i in range(C):
        if board[base + L - 1][i] == 0:
            pos.append(i)
    return random.choice(pos)

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
            break
        clean()

    pboard()

    #print("seq player 2")
    # print(find_seq(2))

    # we play
    move = strat()
    if is_win(1, base):
        print("Gagne")
        break
    print(play(move, 1))
    clean()

    pboard()
