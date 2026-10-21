# Container With Most Water
# LeetCode 11

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maximum_area = 0

        while left < right:
            width = right - left

            current_height = min(
                height[left],
                height[right]
            )

            area = width * current_height

            maximum_area = max(
                maximum_area,
                area
            )

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_area


# Example
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

solution = Solution()
result = solution.maxArea(height)

print("Maximum water area:", result)