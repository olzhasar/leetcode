import functools


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @functools.lru_cache
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            res = pow(x, n // 2)
            return res * res * pow(x, n % 2)

        res = pow(x, abs(n))

        return res if n >= 0 else 1 / res