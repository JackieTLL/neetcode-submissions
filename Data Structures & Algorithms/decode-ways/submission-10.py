class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None] * (len(s) + 1)
        def solve(i):
            if memo[i] is not None:
                return memo[i]
            if i == len(s):
                memo[i] = 1
                return 1
            if s[i] == '0':
                memo[i] = 0
                return 0
            res = solve(i + 1)
            if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                res += solve(i + 2)
            memo[i] = res
            return res
        return solve(0)