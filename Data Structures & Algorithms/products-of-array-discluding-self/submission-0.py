class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                product *= x

        n = len(nums)
        res = [0] * n

        if zero_count >= 2:
            return res

        if zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    res[i] = product
            return res

        for i in range(n):
            res[i] = product // nums[i]

        return res