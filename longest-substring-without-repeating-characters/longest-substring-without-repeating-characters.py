class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        if length <= 1:
            return length

        l = 0
        r = 0
        
        longest = 0

        while r < length:
            if s[r] in s[l:r]:
                while s[l] != s[r]:
                    l += 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest