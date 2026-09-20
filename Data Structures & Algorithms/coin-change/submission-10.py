class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def solve(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            best = float('inf')
            for coin in coins:
                solution = solve(amount - coin)
                if solution != -1:
                    best = min(best, 1 + solution)
                if best == float('inf'):
                    memo[amount] = -1
                else:
                    memo[amount] = best
            return memo[amount]
        return solve(amount)
        