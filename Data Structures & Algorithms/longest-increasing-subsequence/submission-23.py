class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = dict()
        n = len(nums)
        def solve(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0
            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + solve(j))
            memo[i] = best
            return memo[i]
        best = 0
        for i in range(n):
            best = max(best, solve(i))
        return best