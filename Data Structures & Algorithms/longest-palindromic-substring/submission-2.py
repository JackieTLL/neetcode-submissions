class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        memo = [[False] * n for _ in range(n)]

        maxLen = 1
        res = s[0]

        # 长度 1
        for i in range(n):
            memo[i][i] = True

        # 长度 2
        for i in range(1, n):
            if s[i] == s[i - 1]:
                memo[i - 1][i] = True

                if maxLen < 2:
                    maxLen = 2
                    res = s[i - 1:i + 1]

        # 长度 >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True

                    if length > maxLen:
                        maxLen = length
                        res = s[i:j + 1]

        return res