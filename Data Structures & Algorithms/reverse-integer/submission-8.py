class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            multiple = 1
        elif x < 0:
            multiple = -1
        else:
            return 0
        x = abs(x)
        res = 0
        while x != 0:
            n = x % 10
            res = 10 * res + n
            x //= 10
        if res > 2 ** 31 - 1:
            return 0 
        return multiple * res

        