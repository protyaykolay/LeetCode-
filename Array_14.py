# Find Missing and Repeated Values
# LeetCode 2965

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        total_numbers = n * n
        xor_all = 0

        # XOR all numbers in the grid
        for row in grid:
            for num in row:
                xor_all ^= num

        # XOR numbers from 1 to n*n
        for i in range(1, total_numbers + 1):
            xor_all ^= i

        # Find the rightmost set bit
        mask = xor_all & -xor_all

        first_group = 0
        second_group = 0

        # Divide grid numbers into two groups
        for row in grid:
            for num in row:
                if num & mask:
                    first_group ^= num
                else:
                    second_group ^= num

        # Divide expected numbers into two groups
        for i in range(1, total_numbers + 1):
            if i & mask:
                first_group ^= i
            else:
                second_group ^= i

        # Identify the repeated and missing numbers
        for row in grid:
            for num in row:
                if num == first_group:
                    return [first_group, second_group]
                elif num == second_group:
                    return [second_group, first_group]

        return []


# Example
grid = [[1, 3], [2, 2]]

solution = Solution()
result = solution.findMissingAndRepeatedValues(grid)

print("Repeated and missing numbers:", result)