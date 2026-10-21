# Search in Rotated Sorted Array
# LeetCode 33

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target exists in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Search the right half
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target exists in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Search the left half
                else:
                    right = mid - 1

        return -1


# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

solution = Solution()
result = solution.search(nums, target)

print("Target index:", result)