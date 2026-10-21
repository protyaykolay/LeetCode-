# Three Sum
# LeetCode 15

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


# Example
nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
result = solution.threeSum(nums)

print("Triplets whose sum is zero:", result)