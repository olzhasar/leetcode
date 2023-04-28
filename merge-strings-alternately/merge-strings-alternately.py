class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)

        l, r = 0, 0
        output = []

        while l < len_1 or r < len_2:
            if l < len_1:
                output.append(word1[l])
                l += 1
            if r < len_2:
                output.append(word2[r])
                r += 1

        return "".join(output)