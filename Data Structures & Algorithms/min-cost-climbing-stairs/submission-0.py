class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [float('inf')] * (1 + len(cost))
        minCost[0] = minCost[1] = 0

        for i in range(2, 1 + len(cost)):
            minCost[i] = min(minCost[i - 1] + cost[i - 1], minCost[i - 2] + cost[i - 2])

        return minCost[len(cost)]