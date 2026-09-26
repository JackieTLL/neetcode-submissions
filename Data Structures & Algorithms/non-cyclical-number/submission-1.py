class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            new = 0
            while n != 0:
                new += (n % 10) ** 2
                n //= 10
            if new in seen:
                return False
            seen.add(new)
            n = new
        return True
        