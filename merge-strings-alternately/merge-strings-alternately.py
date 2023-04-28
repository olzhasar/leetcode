class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_1, len_2 = len(word1), len(word2)

        l, r = 0, 0
        output = ""

        while l < len_1 or r < len_2:
            if l < len_1:
                output += word1[l]
                l += 1
            else:
                output += word2[r:]
                break
            if r < len_2:
                output += word2[r]
                r += 1
            else:
                output += word1[l:]
                break

        return output