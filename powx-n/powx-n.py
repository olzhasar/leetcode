class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            res = pow(x, n // 2)
            res *= res
            if n % 2 != 0:
                res *= x
            return res

        if n < 0:
            x = 1 / x

        return pow(x, abs(n))