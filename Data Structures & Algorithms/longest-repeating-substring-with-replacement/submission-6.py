class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        highestFreq = 0
        freqCh = ''
        left, right = 0, 0
        while right < len(s):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1
            if count[ch] > highestFreq:
                highestFreq = count[ch]
                freqCh = ch
            if right - left + 1 - highestFreq <= k:
                res = max(res, right - left + 1)
                right += 1
            else:
                removeCh = s[left]
                count[removeCh] -= 1
                if removeCh == freqCh:
                    highestFreq -= 1
                left += 1
                right += 1
        return res
        