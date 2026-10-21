# Spiral Matrix
# LeetCode 54

class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        result = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1. Move Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            top += 1

            # 2. Move Down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            right -= 1

            # 3. Move Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])

                bottom -= 1

            # 4. Move Up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                left += 1

        return result


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()

result = solution.spiralOrder(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("Spiral Order:", result)