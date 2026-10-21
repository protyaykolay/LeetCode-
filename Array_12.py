# Two Sum
# LeetCode 1

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists
            if complement in num_map:
                return [num_map[complement], i]

            # Store the number and its index
            num_map[num] = i

        return []


# Example
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print("Indices of the two numbers:", result)