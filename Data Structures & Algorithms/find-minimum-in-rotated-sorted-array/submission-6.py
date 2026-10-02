class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        n = len(nums)
        half = n // 2
        left = nums[:half]
        right = nums[half:]
        if right and right[0] > right[-1]:
            return self.findMin(right)
        elif left and left[0] > left[-1]:
            return self.findMin(left)
        else:
            return right[0]