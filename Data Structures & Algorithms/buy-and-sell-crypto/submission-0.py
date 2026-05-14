class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize buy and profit variables
        buy = profit = 0
        # Sliding-window approach
        for sell in range(1, len(prices)):
            # Compute the potential profits
            potential = prices[sell] - prices[buy]
            if potential > 0:
                # See if potential is better than current profit
                profit = max(profit, potential)
            # Cheaper to buy today than earlier
            else:
                buy = sell
        # Return max profit
        return profit