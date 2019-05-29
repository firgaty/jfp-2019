def cp_move():
    return 0

while(True):

    move = int(input())

    if move < 0:
        play(3, 1)
        continue

    play(move, 2)
    play(cp_move, 1)

    print()
