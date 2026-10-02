class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Base case  
        dp = [float('inf')] * (1 + amount)
        dp[0] = 0 
        # Bottom-up DP
        for subAmt in range(1, len(dp)):
            for coin in coins:
                if subAmt >= coin and dp[subAmt] > dp[subAmt - coin] + 1:
                    dp[subAmt] = dp[subAmt - coin] + 1
        return dp[amount] if dp[amount] < float('inf') else -1

