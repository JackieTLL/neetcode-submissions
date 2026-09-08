class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        first = nums[0]
        other = nums[1:]
        return [oneDList[:i] + [first] + oneDList[i:]
                for oneDList in self.permute(other) 
                for i in range(len(other) + 1)]
        