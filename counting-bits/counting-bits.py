import functools


class Solution:
    def countBits(self, n: int) -> List[int]:
        @functools.lru_cache
        def num_bits(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return num_bits(n // 2) + n % 2

        return [num_bits(i) for i in range(n + 1)]