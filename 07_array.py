# Island Perimeter
# LeetCode 463

class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:

                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1       # up

                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1       # down

                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1       # left

                    if j == cols - 1 or grid[i][j + 1] == 0:
                        perimeter += 1       # right

        return perimeter


# Example
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

solution = Solution()

result = solution.islandPerimeter(grid)

print("Island Perimeter:", result)