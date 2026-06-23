class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            key = [0] * 26
            for ch in i:
                key[ord(ch)-ord('a')] += 1
            res[tuple(key)].append(i)
        return list(res.values())
