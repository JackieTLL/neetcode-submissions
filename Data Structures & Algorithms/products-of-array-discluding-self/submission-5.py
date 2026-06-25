class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        pref[0] = 1
        pref[1] = nums[0]
        suff[-1] = 1
        suff[-2] = nums[-1]
        for i in range(2, n):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res