class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in needed:
                return [needed[need], i]
            needed[nums[i]] = i
            