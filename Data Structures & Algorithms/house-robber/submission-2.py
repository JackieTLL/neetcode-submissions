class Solution:
    def rob(self, nums: List[int]) -> int:
        rep = dict()
        n = len(nums)
        def solve(i, nums):
            if i == n - 1: 
                return nums[i]
            if i == n - 2:
                return max(nums[i], nums[i + 1])
            if i + 1 not in rep.keys():
                rep[i + 1] = solve(i + 1, nums)
            if i + 2 not in rep.keys():
                rep[i + 2] = solve(i + 2, nums)
            return max(nums[i] + rep[i + 2], rep[i + 1])
            
        return solve(0, nums)
        