import functools


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @functools.cache
        def backtrack(current=0, start=0):
            if current == n:
                return 1

            res = 0

            remaining = n - 1 - current
            for i in range(start, m - remaining):
                if s[i] == t[current]:
                    res += backtrack(current + 1, i + 1)

            return res

        return backtrack()