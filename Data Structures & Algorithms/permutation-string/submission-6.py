class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def zeroDict(count):
            for key in count:
                if count[key] != 0:
                    return False
            return True
        if len(s2) < len(s1):
            return False
        n = len(s1)
        count = dict()
        for i in range(n):
            count[s1[i]] = count.get(s1[i], 0) + 1
        for i in range(n):
            if s2[i] in count:
                count[s2[i]] -= 1 
        for i in range(len(s2) - n):
            if zeroDict(count):
                return True
            if s2[n + i] in count:
                count[s2[n + i]] -= 1
            if s2[i] in count:
                count[s2[i]] += 1
        return zeroDict(count)
