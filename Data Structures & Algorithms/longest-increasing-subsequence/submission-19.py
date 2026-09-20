class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = dict()
        n = len(nums)
        def solve(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0
            k = -1
            best = float('-inf')
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    k = j
                    solution = solve(k)
                    best = max(best, 1 + solve(k))
            if best == float('-inf'):
                memo[i] = 1
            else:
                memo[i] = best
            return memo[i]
        best = 1
        for i in range(n):
            best = max(best, solve(i))
        return best