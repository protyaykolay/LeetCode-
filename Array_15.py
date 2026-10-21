# Kth Largest Element in an Array
# LeetCode 215

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # Keep only the k largest elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2

solution = Solution()
result = solution.findKthLargest(nums, k)

print("Kth largest element:", result)