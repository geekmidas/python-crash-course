# def draw_state_matrix(slots):
#     for row in slots:
#         line = '|'
#         for marker in row:
#             line += marker + '|'
#         print(line)
def draw_state(slots):
    for row in slots:
        line = '|'+'|'.join(row)+'|'
        print(line)

def generate_initial(size = 3):
    matrix = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append('-')
        matrix.append(row)
    return matrix

def play(slots, marker):
    # Place marker in the correct position
    move = input('Place your marker at (x,y): ')
    x,y = move.split(',')
    i,j = int(x),int(y)
    slot = slots[i - 1][j - 1]
    if slot == '-':
        slots[i - 1][j - 1] = marker
        draw_state(slots)
    else:
        play(slots, marker)
    # draw_state(slots)

def tic_tac_toe():
    # Game logic
    pass