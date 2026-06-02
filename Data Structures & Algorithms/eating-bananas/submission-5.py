class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Get default pointers of the eating rate space
        l, r = 1, max(piles)
        # Binary search on the eating rate space
        while l < r:
            # Compute the average eating rate
            k = (l + r) // 2
            # Tabulate the upper time for k rate
            t = 0
            for p in piles:
                t += math.ceil(p / k)
            # Divide space for k is SLOW
            if t > h:
                l = k + 1
            # Divide space for k is FAST
            else:
                r = k
        # Return the minimum eating rate 
        return l

