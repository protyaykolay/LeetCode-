# Rotate Array by K Steps
# LeetCode 189

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        if n == 0:
            return

        k %= n

        # Reverse the entire array
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = nums[:k][::-1]

        # Reverse the remaining elements
        nums[k:] = nums[k:][::-1]


# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution = Solution()
solution.rotate(nums, k)

print("Array after rotation:", nums)