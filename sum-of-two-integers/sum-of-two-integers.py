class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        sign_bit = 0x80000000

        while b != 0:
            s = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a, b = s, carry

        if a & sign_bit:
            a = a | ~mask

        return a