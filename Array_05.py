# Best Time to Buy and Sell Stock
# LeetCode 121

class Solution(object):
    def maxProfit(self, prices):
        buy = float('inf')
        profit = 0

        for price in prices:
            if price < buy:
                buy = price

            elif price - buy > profit:
                profit = price - buy

        return profit


# Example
prices = [7, 1, 5, 3, 6, 4]

solution = Solution()

result = solution.maxProfit(prices)

print("Prices:", prices)
print("Maximum Profit:", result)
























