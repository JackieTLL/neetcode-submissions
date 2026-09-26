class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        def SW(i, currSum):
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            if i == len(nums) - 1:
                if currSum == target:
                    return 1
                else:
                    return 0
            res = SW(i + 1, currSum + nums[i + 1]) + SW(i + 1, currSum - nums[i + 1])
            memo[(i, currSum)] = res
            return res
        return SW(-1, 0)
        