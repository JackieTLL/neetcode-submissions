class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topK = []
        self.k = k
        while nums != []:
            heapq.heappush(self.topK, nums.pop())
            if len(self.topK) > k:
                heapq.heappop(self.topK)

    def add(self, val: int) -> int:
        heapq.heappush(self.topK, val)
        if len(self.topK) > self.k:
            heapq.heappop(self.topK)
        return self.topK[0]
        
