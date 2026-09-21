class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def solve(start, target):
            if target == 0:
                res.append(path[:])
                return None
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if target < candidates[i]:
                    break
                path.append(candidates[i])
                solve(i + 1, target - candidates[i])
                path.pop()
        solve(0, target)
        return res
        