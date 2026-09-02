import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Eaten(piles, speed, h):
            total = 0
            for v in piles:
                total += math.ceil(v/speed)
            return total <= h
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if Eaten(piles, m, h):
                r = m - 1
            else:
                l = m + 1
        return l
        