# Maximum Product Subarray
# LeetCode 152

class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If the current number is negative,
            # swap maximum and minimum products
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result


# Example
nums = [2, 3, -2, 4]

solution = Solution()
result = solution.maxProduct(nums)

print("Maximum product subarray:", result)