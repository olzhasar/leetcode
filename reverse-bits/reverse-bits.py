class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31

        while n:
            if n & 1 == 1:
                result += 2 ** power
            n = n >> 1
            power -= 1

        return result