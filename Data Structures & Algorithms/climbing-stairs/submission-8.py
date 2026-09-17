class Solution:
    def climbStairs(self, n: int) -> int:
        repository = dict()
        def solve(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n - 1 not in repository.keys():
                repository[n - 1] = solve(n - 1)
            if n - 2 not in repository.keys():
                repository[n - 2] = solve(n - 2)
            return repository[n - 1] + repository[n - 2]
        return solve(n)
        