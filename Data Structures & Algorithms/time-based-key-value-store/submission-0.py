from bisect import bisect_left
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.wordDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.wordDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.wordDict[key]
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                l = m + 1
                res = arr[m][0]
            else:
                r = m - 1
        return res
