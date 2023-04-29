class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        i = 0

        while True:
            try:
                char = strs[0][i]
                for s in strs[1:]:
                    if s[i] != char:
                        return prefix
            except IndexError:
                return prefix
            prefix += char
            i += 1

        return prefix