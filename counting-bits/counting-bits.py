class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        def num_bits(n):
            if n == 0:
                return 0
            return result[n // 2] + n % 2

        for i in range(n + 1):
            result.append(num_bits(i))

        return result