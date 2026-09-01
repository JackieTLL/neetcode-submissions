class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search1DList(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                i = (l + r) // 2
                if nums[i] == target:
                    return True
                elif nums[i] < target:
                    l = i + 1
                else:
                    r = i - 1
            return False
        l, r = 0, len(matrix) - 1
        row = -1
        while l <= r:
            i = (l + r) // 2
            if matrix[i][0] <= target:
                row = i
                l = i + 1
            else:
                r = i - 1
        if row == -1:
            return False
        return search1DList(matrix[row], target)

        