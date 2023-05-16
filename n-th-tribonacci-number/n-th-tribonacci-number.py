class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}

        def helper(n):
            if n not in cache:
                cache[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
            return cache[n]

        return helper(n)