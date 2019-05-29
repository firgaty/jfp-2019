# top line is 0
board = [[0] * 7 for _ in range(7)]

# 0 == nothing
# otherwise == player
def play(c, p):
    for i in range(7):
        if board[i][c] != 0:
            assert (i != 0)
            board[i - 1][c] = p
            return

    board[6][c] = p

def find_seq_aux(p, dx, dy):
    seqs = []
    for i in range(7):
        for j in range(7):
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
    seqs = find_seq_aux(p, 1, 0)         # horiziontals
    seqs.extend(find_seq_aux(p, 0, 1))  # verticals
    seqs.extend(find_seq_aux(p, 1, 1))  # diags
    seqs.extend(find_seq_aux(p, -1, 1)) # anti diags
    seqs.sort(key=lambda x: len(x))
    return seqs

def cp_move():
    return 0

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

    pboard()

    print("seq player 2")
    print(find_seq(2))
        
    # we play
    move = cp_move()
    play(move, 1)
    
    print(move)
    pboard()
