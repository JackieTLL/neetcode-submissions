class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = set()
        for v in nums:
            if v not in occ:
                occ.add(v)
            else:
                return True
        return False
        