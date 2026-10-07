class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for v in nums:
            if len(pq) == k:
                poppedV = heapq.heappop(pq)
                heapq.heappush(pq, max(v, poppedV))
            else:
                heapq.heappush(pq, v)
        return heapq.heappop(pq)