# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while True:
            val = (l + r) // 2

            result = guess(val)
            if result == 0:
                return val
            if result == 1:
                l = val + 1
            else:
                r = val - 1