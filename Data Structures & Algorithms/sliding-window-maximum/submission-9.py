class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        right = 0
        while right < len(nums):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            while q and (nums[q[0]] < nums[q[-1]] or q[0] <= right - k):
                q.popleft()
            if right >= k - 1:
                res.append(nums[q[0]])
            right += 1
        return res
