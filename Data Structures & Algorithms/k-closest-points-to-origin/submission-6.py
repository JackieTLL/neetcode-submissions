class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        pq = []
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        for point in points:
            heapq.heappush(pq, (-distance(point), point))
            if len(pq) > k:
                heapq.heappop(pq)
        # while pq != []:
        #     res.append(heapq.)
        return [pq[i][1] for i in range(len(pq))]
