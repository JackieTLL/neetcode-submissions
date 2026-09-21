class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def solve(start, target):
            if target == 0:
                res.append(path[:])
                return None
            if target < 0:
                return None
            for i in range(start, len(nums)):
                path.append(nums[i])
                solve(i, target - nums[i])
                path.pop()
        solve(0, target)
        return res
        
        
