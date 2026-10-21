# Remove Duplicate element in array
# LeetCode 26

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# Example
nums = [1, 1, 2, 2, 3, 4, 4]

solution = Solution()

k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])