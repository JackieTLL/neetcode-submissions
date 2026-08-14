class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = []
        startNum = []
        for num in nums:
            if (num - 1) not in numsSet:
                startNum.append(num)
        for num in startNum:
            l = [num]
            while (l[-1] + 1) in numsSet:
                l.append(l[-1] + 1)
            if len(l) > len(res):
                res = l
        return len(res)


        