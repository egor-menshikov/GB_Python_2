# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]


def transpose(matrix):
    new_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


print(*transpose(matrix), sep='\n')
