# Rotate Image
# LeetCode 48

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i], matrix[i][j]
                )

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
solution.rotate(matrix)

print("Matrix after 90-degree clockwise rotation:")
for row in matrix:
    print(row)