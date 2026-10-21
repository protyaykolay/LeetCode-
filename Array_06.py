# Move Zeroes
# LeetCode 283

class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# Example
nums = [0, 1, 0, 3, 12]

solution = Solution()

solution.moveZeroes(nums)

print("Array after moving zeroes:", nums)

        
















