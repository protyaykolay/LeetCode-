# Find Minimum in Rotated Sorted Array
# LeetCode 153

class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is on the right side
                left = mid + 1
            else:
                # Minimum is at mid or on the left side
                right = mid

        return nums[left]


# Example
nums = [3, 4, 5, 1, 2]

solution = Solution()
result = solution.findMin(nums)

print("Minimum element:", result)