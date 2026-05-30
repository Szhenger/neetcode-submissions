class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Get a default profit variable
        maxProfit = 0
        # Compute the optimal buy and sell days for NeetCoin
        buy = 0
        for sell in range(1, len(prices)):
            # Compute the potential profit
            profit = prices[sell] - prices[buy]
            # Case 1: Gain profit
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            # Case 2: Lose profit
            else:
                buy = sell
        # Return the max profit
        return maxProfit