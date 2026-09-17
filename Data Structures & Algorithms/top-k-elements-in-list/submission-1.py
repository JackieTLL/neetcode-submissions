class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for v in nums:
            count[v] = count.get(v, 0) + 1
        pq = []
        for num in count.keys():
            heapq.heappush(pq, (count[num], num))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        for freq, num in pq:
            res.append(num)
        return res