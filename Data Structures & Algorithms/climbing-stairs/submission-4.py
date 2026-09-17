class Solution:
    def climbStairs(self, n: int) -> int:
        repository = dict()
        def solve(i, n):
            if i >= n:
                return 0
            if i == n - 1:
                return 1
            if i == n - 2:
                return 2
            if i + 1 not in repository.keys():
                repository[i + 1] = solve(i + 1, n)
            if i + 2 not in repository.keys():
                repository[i + 2] = solve(i + 2, n)
            return repository[i + 1] + repository[i + 2]
        return solve(0, n)
        