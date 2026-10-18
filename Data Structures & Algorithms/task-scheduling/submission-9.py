class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        count = dict()
        for v in tasks:
            count[v] = count.get(v, 0) + 1
        pq = [-freq for freq in count.values()]
        heapq.heapify(pq)
        while pq:
            temp = []
            executed = 0
            for _ in range(n + 1):
                if not pq:
                    break
                freq = heapq.heappop(pq)
                freq += 1
                executed += 1
                if freq < 0:
                    temp.append(freq)
            for freq in temp:
                heapq.heappush(pq, freq)
            if pq:
                res += n + 1
            else:
                res += executed
        return res
                