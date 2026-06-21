class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict() # letter->count
        count_t = dict()
        for element in s:
            if element in count_s:
                count_s[element] += 1
            else:
                count_s[element] = 1
        for element in t:
            if element in count_t:
                count_t[element] += 1
            else:
                count_t[element] = 1
        return count_s == count_t
