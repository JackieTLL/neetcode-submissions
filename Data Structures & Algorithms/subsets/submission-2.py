class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        first = nums[0]
        other = nums[1:]
        tempSet = self.subsets(other)
        return [[first] + subSet for subSet in tempSet] + tempSet
        