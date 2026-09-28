class MedianFinder:

    def __init__(self):
        self.pqUpper = []
        self.pqLower = []
        self.median = float('-inf')

    def addNum(self, num: int) -> None:
        if len(self.pqUpper) == len(self.pqLower):
            heapq.heappush(self.pqUpper, num)
            if self.pqLower != [] and -self.pqLower[0] > self.pqUpper[0]:
                heapq.heappush(self.pqUpper, -heapq.heappop(self.pqLower))
                heapq.heappush(self.pqLower, -heapq.heappop(self.pqUpper))
            self.median = self.pqUpper[0]
        else:
            heapq.heappush(self.pqLower, -num)
            if -self.pqLower[0] > self.pqUpper[0]:
                heapq.heappush(self.pqUpper, -heapq.heappop(self.pqLower))
                heapq.heappush(self.pqLower, -heapq.heappop(self.pqUpper))
            self.median = (self.pqUpper[0] - self.pqLower[0]) / 2
    def findMedian(self) -> float:
        return float(self.median)
        
        