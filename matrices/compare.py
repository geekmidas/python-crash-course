data = [[0,0,0], [0,1,1], [0,1,0]]

def compare_row(matrix):
    for row in matrix:
        prev = row[0]
        winner = True
        for current in row[1:]:
            if current != prev:
                winner = False
                break
            prev = current
        if winner:
            return prev

def compare_cols(matrix):
    matrix_zip = zip(*matrix)

    return compare_row(matrix_zip)

print(compare_cols(data))