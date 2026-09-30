class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None] * (len(s) + 1)
        def solve(i):
            if i == len(s):
                memo[i] = True
                return True
            if memo[i] != None:
                return memo[i]
            for word in wordDict:
                if s.startswith(word, i):
                    solution = solve(i + len(word))
                    if solution:
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return solve(0)
        