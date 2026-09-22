class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = dict()
        memo2 = dict()
        if len(nums) == 1:
            return nums[0]
        def solve(i, nums, memo):
            n = len(nums)
            if i == n - 1: 
                return nums[i]
            if i == n - 2:
                return max(nums[i], nums[i + 1])
            if i + 1 not in memo.keys():
                memo[i + 1] = solve(i + 1, nums, memo)
            if i + 2 not in memo.keys():
                memo[i + 2] = solve(i + 2, nums, memo)
            return max(nums[i] + memo[i + 2], memo[i + 1])
            
        return max(solve(0, nums[1:], memo1), solve(0, nums[:-1], memo2))
        