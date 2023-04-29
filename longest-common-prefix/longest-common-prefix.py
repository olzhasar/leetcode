class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        min_length = min((len(s) for s in strs))

        for i in range(min_length):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return prefix
            prefix += char

        return prefix