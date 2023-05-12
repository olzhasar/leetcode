class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        i = 0
        while i < 32 and n > 0:
            if n % 2 == 1:
                result += 2 ** (31 - i)
            n //= 2
            i += 1

        return result