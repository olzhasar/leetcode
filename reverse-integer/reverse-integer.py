class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        negative = x < 0
        x = abs(x)
        lim = 2 ** 31 // 10
        
        while x >= 10:
            r = r * 10 + x % 10
            x //= 10

        if r >= lim and x:
            if r > lim:
                return 0
            if x > 8 or (not negative and x > 7):
                return 0

        r = r * 10 + x % 10

        if negative:
            return -r
        return r