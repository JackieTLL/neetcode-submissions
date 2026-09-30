class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 == 1:
            return False
        half = summation / 2
        memo = dict()
        def solve(i, remain):
            if (i, remain) in memo:
                return memo[(i, remain)]
            if remain == 0:
                memo[(i, remain)] = True
                return True
            if i == len(nums) or remain < 0:
                memo[(i, remain)] = False
                return False
            res = solve(i + 1, remain - nums[i]) or solve(i + 1, remain)
            memo[(i, remain)] = res
            return res
        return solve(0, half)
        