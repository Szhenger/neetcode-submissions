class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Get default pointers of the eating rate space
        l, r = 1, max(piles)
        # Binary search on the eating rate space
        while l < r:
            k = (l + r) // 2
            # Compute the time for k bananas-per-hour
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            # Case 1: k is SLOW
            if t > h:
                l = k + 1
            # Case 2: k is FAST
            else:
                r = k
        return r

