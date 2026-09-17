class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            tmp = [0] * 26
            for ch in word:
                tmp[ord(ch) - ord('a')] += 1
            res[tuple(tmp)].append(word)
        return list(res.values())