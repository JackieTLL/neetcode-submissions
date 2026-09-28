class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        while stones != []:
            heapq.heappush(pq, -stones.pop())
        while len(pq) >= 2:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -abs(x-y))
        return -pq[0] if pq != [] else 0
        