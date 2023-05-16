class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        one, two, three = 0, 1, 1

        for _ in range(3, n + 1):
            result = one + two + three
            one, two, three = two, three, result

        return result