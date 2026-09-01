class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        lastI, lastH = 0, 0
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append([i, h])
            else:
                while stack and h < stack[-1][1]:
                    maxArea = max(maxArea, (i - stack[-1][0]) * stack[-1][1])
                    lastI, lastH = stack.pop()
                stack.append([lastI, h])
        for k in range(len(stack)):
            i = stack[k][0]
            h = stack[k][1]
            maxArea = max(maxArea, h * (len(heights) - stack[k][0]))

        return maxArea
        