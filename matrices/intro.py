matrix = [[1,2,3], [4,5,6], [7,8,9]]
# [1,2,3]
# for row in matrix:
#     for x in row:
#         print(x)
# for i,row in enumerate(matrix): # [i][j], [j][i]
#     for j, col in enumerate(row):
#         matrix[j]
#         print(matrix[j][i])
matrix = [[1,0,0], [1,1,1], [0,1,1]]
for i in range(3): # [i][j], [j][i]
    for j in range(3):
        row_j = matrix[j]
        print(row_j[i])

matrix_zip = zip(*matrix)
print(list(matrix_zip))
for col in zip(*matrix):
    pass
# 1 2 3
# 1 1 1
# 7 8 9