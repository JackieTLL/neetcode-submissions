class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = dict()
        def solve(s):
            if s == '':
                memo[s] = True
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                if s.startswith(word):
                    solution = solve(s[len(word):])
                    if solution:
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return solve(s)
        