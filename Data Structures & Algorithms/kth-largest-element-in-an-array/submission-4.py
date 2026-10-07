class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for v in nums:
            if len(pq) < k:
                heapq.heappush(pq, v)
            else:
                heapq.heappushpop(pq, v)
        return pq[0]