class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[None] * (n + 1) for _ in range(m + 1)]
        def LCS(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            if i == m or j == n:
                memo[i][j] = 0
                return 0
            if text1[i] == text2[j]:
                res = LCS(i + 1, j + 1)
                memo[i][j] = 1 + res
                return 1 + res
            else:
                res = max(LCS(i + 1, j), LCS(i, j + 1))
                memo[i][j] = res
                return res
        return LCS(0, 0)
            
        