class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1, len_2 = len(str1), len(str2)

        for l in range(min(len_1, len_2), 0, -1):
            if len_1 % l != 0 or len_2 % l != 0:
                continue

            val = str1[:l]

            n1, n2 = len_1 // l, len_2 // l

            if str1 == n1 * val and str2 == n2 * val:
                return val
                        
        return ""