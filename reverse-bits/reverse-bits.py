class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32

        i = 0
        while i < 32 and n > 0:
            bits[i] = n % 2
            n //= 2
            i += 1

        power = 31

        result = 0

        for b in bits:
            if b == 1:
                result += 2 ** power
            power -= 1

        return result