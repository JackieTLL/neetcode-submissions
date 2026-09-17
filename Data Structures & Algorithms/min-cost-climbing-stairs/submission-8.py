class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        rep = dict()
        n = len(cost)
        def solve(i, cost):
            if i == n - 1:
                return cost[-1]
            if i == n - 2:
                return cost[-2]
            if i + 1 not in rep.keys():
                rep[i + 1] = solve(i + 1, cost)
            if i + 2 not in rep.keys():
                rep[i + 2] = solve(i + 2, cost)
            return cost[i] + min(rep[i + 1], rep[i + 2])
        solve(-1, cost)
        return min(rep[0], rep[1])
        