"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        tmp = []
        for interval in intervals:
            tmp.append((interval.start, interval.end))
        tmp.sort()
        for i in range(1, len(tmp)):
            if tmp[i][0] < tmp[i - 1][1]:
                return False
        return True
