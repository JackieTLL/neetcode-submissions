class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        movingLen = 0
        seen = dict()
        k = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in seen and seen[ch] >= k:
                movingLen = i - seen[ch] - 1
                k = seen[ch]
            seen[ch] = i
            movingLen += 1
            maxLen = max(maxLen, movingLen)
        return maxLen
        