class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        stack = []
        for interval in intervals:
            if not stack or interval[0] >= stack[-1][1]:
                stack.append(interval)
            elif interval[1] < stack[-1][1]:
                stack[-1] = interval
        return len(intervals) - len(stack)
