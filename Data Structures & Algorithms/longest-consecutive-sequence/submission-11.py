class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        startNum = []
        for num in numsSet:
            if (num - 1) not in numsSet:
                startNum.append(num)
        for num in startNum:
            length = 1
            while num + length in numsSet:
                length += 1
            res = max(res, length)
        return res


        