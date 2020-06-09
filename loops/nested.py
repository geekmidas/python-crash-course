matrix = [['1','2','3'],['4','5','6'],['7','8','9']]
# 1 2 3
# 4 5 6
# 7 8 9
# for row in matrix:
#     line = ''
#     for i in row:
#         line += ' ' + str(i)
#     clean = line.lstrip()
#     print(len(clean), clean)
#     print(len(line), line)

for row in matrix:
    print(' '.join(row))
