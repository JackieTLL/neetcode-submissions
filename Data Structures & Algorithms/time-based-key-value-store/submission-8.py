from bisect import bisect_right
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.wordDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.wordDict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.wordDict[key]
        i = bisect_right(arr, (timestamp, chr(127))) - 1
        if i < 0:
            return ""
        res = arr[i][1]
        return res
