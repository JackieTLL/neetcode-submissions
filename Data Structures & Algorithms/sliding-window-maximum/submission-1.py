class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []
        runningMax = float('-inf')
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))
        right = k-1
        while right < len(nums):
            heapq.heappush(pq, ((-nums[right], right)))
            while pq and pq[0][1] <= right - k:
                heapq.heappop(pq)
            runningMax = -pq[0][0]
            res.append(runningMax)
            right += 1
        return res
            