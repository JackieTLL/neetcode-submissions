class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        max_l = 0
        max_r = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    res += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    res += max_r - height[r]
                r -= 1
        return res
            
                
        