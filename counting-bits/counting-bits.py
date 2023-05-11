class Solution:
    def countBits(self, n: int) -> List[int]:
        def num_bits(n):
            count = 0
            while n > 0:
                count += n % 2
                n = n // 2
            return count

        return [num_bits(i) for i in range(n + 1)]