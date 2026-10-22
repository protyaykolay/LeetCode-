# Set Matrix Zeroes
# LeetCode 73

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        # Step 1: Find all zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 2: Set rows to zero
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Step 3: Set columns to zero
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0


# Example
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

solution = Solution()
solution.setZeroes(matrix)

print("Matrix after setting zeroes:")
for row in matrix:
    print(row)