class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        k = 31
        while k >= 0:
            res += n % 2 * 2 ** k
            n //= 2
            k -= 1
        return res
        