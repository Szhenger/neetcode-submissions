class Solution:
    def climbStairs(self, n: int) -> int:
        fib0 = fib1 = 1
        for _ in range(n - 1):
            fib0, fib1 = fib1, fib0 + fib1
        return fib1