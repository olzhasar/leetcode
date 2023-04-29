class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length <= 1:
            return length

        l = 0
        r = 0
        
        longest = 0

        current = ""

        while r < len(s):
            if s[r] in current:
                while s[l] != s[r]:
                    l += 1
                l += 1
            current = s[l:r + 1]
            longest = max(longest, r - l + 1)
            r += 1

        return longest