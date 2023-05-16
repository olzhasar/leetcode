import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        @functools.cache
        def num_ways(amount, start=0):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            num = 0
            for i, c in enumerate(coins[start:], start):
                if c == amount:
                    num += 1
                elif c < amount:
                    num += num_ways(amount - c, i)
                else:
                    break
            return num

        return num_ways(amount)