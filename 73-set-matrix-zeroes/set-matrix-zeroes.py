
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Find all rows and columns containing zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set the corresponding rows to zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Set the corresponding columns to zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
