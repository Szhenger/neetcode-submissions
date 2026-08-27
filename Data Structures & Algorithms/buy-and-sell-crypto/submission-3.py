class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = buyDay = 0
        for sellDay in range(1, len(prices)):
            curPro = prices[sellDay] - prices[buyDay]
            if curPro > 0:
                maxPro = max(maxPro, curPro)
            else:
                buyDay = sellDay
        return maxPro
