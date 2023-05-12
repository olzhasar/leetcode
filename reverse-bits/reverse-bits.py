class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        i = 0
        while n > 0:
            result += n % 2 * 2 ** (31 - i)
            n //= 2
            i += 1

        return result