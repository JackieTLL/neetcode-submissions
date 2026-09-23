class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for j in range(n):
            for i in range(0, j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    res += 1
                    dp[i][j] = True
        return res