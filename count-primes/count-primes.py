class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Array of all prime numbers, True - prime, False - composite
        numbers = [False, False] + [True] * (n - 2)
        # Iterate from 2 (smallest prime) to square root of n. Any value greater than square root will be covered automatically by smaller numbers
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Mark all multiples of p from p**2 to n as composite
                # We start with p**2 because anything between p and p**2 will be automatically covered by smaller primes
                # E.g. for 5: 10, 15, 20 are covered by 2 and 3
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        return sum(numbers)