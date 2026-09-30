class Solution:
    def countBits(self, n: int) -> List[int]:
        def numOnes(n):
            res = 0
            while n > 0:
                res += n % 2
                n //= 2
            return res
        res = []
        for i in range(n + 1):
            res.append(numOnes(i))
        return res
        