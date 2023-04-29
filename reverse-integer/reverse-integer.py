class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        negative = x < 0

        x = abs(x)

        while x:
            digits.append(x % 10)
            x = x // 10

        for i, digit in enumerate(reversed(digits)):
            x += digit * (10 ** i)

        if negative:
            x = -x

        if x <= -2**31 or x >= 2**31 - 1:
            return 0

        return x