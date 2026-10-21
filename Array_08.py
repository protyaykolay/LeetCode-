# Maximum Subarray - Kadane's Algorithm
# LeetCode 53

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]

        for i in nums[1:]:
            if current_sum < 0:
                current_sum = 0

            current_sum = current_sum + i
            max_sum = max(max_sum, current_sum)

        return max_sum


# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()

result = solution.maxSubArray(nums)

print("Array:", nums)
print("Maximum Subarray Sum:", result)