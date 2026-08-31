class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()
        stack = []
        for p, s in pair[::-1]:
            if not stack:
                stack.append([p, s])
            else:
                t1 = (target - stack[-1][0]) / stack[-1][1]
                t2 = (target - p) / s
                if t1 < t2:
                    stack.append([p, s])
        return len(stack)

        