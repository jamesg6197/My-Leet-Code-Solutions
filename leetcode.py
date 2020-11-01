//Rotate Image


def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        columns = []
        for columnnum in range(n):
            column = []
            for row in matrix:
                column.append(row[columnnum])
            columns.append(column)
        for rownum in range(n):
            for element in range(n):
                column = columns[rownum]
                celement = column[(-1*element) - 1]
                matrix[rownum][element] = celement
