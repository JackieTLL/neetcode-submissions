class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for ch in s:
            if ch.isalnum():
                t += ch.lower()
        for i in range(len(t) // 2):
            if t[i] != t[- i - 1]:
                return False
        return True
        