class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialization of dict
        count = dict()
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        bestLeft, bestRight = 0, 0
        minLen = float('inf')
        left = 0
        missing = len(t)
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1
                if count[s[right]] >= 0:
                    missing -= 1
            while missing == 0:
                if s[left] not in count:
                    left += 1
                elif count[s[left]] < 0:
                    count[s[left]] += 1
                    left += 1
                else:
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        bestLeft, bestRight = left, right
                    break
        if minLen == float('inf'):
            return ""
        return s[bestLeft: bestRight + 1]
                    
            