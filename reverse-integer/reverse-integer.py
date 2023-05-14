class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        negative = x < 0
        x = abs(x)
        lim = 214748364
        
        while x:
            r = r * 10 + x % 10
            x //= 10
            if r >= lim and x:
                if r > lim:
                    return 0
                if negative and x >= 8:
                    return 0
                elif not negative and x >= 7:
                    return 0

        if negative:
            return -r
        return r