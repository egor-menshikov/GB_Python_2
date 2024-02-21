class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        return '\n'.join(' '.join([f'{x}' for x in row]) for row in self.data)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols}'

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result

    def __mul__(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
