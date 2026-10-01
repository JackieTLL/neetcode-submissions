class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = dict()
        def solve(i, k):
            if (i, k) in memo:
                return memo[(i, k)]
            if i > len(prices) - 1:
                memo[(i, k)] = 0
                return 0
            if k == 0:
                memo[(i, k)] = max(solve(i + 1, 0), solve(i + 1, 1) - prices[i])
                return memo[(i, k)]
            if k == 1:
                memo[(i, k)] = max(prices[i] + solve(i + 2, 0), solve(i + 1, 1))
                return memo[(i, k)]
        return solve(0, 0)