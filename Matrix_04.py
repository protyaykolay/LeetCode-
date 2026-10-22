# Word Search
# LeetCode 79

class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        # DFS function
        def dfs(i, j, index):

            # Entire word found
            if index == len(word):
                return True

            # Check boundaries
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            # Character doesn't match
            if board[i][j] != word[index]:
                return False

            # Mark current cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Search in four directions
            found = (
                dfs(i + 1, j, index + 1) or
                dfs(i - 1, j, index + 1) or
                dfs(i, j + 1, index + 1) or
                dfs(i, j - 1, index + 1)
            )

            # Backtrack: restore original value
            board[i][j] = temp

            return found

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


# Example
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

solution = Solution()
result = solution.exist(board, word)

print("Word found:", result)