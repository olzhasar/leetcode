class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1, len_2 = len(str1), len(str2)

        for l in range(min(len_1, len_2), 0, -1):
            if len_1 % l != 0 or len_2 % l != 0:
                continue

            val = str1[:l]
            k = 0
            failed = False

            while k + l <= len_1 or k + l <= len_2:
                if k + l <= len_1:
                    if str1[k: k + l] != val:
                        failed = True
                        break
                if k + l <= len_2:
                    if str2[k: k + l] != val:
                        failed = True
                        break
                k += l

            if not failed:
                return val
                        
        return ""