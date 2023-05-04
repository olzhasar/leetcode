class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        l = 0
        r = len(s) - 1

        output = [None] * (r + 1)

        while l <= r:
            if l == r:
                output[l] = s[l]
                break
            elif s[l].lower() not in vowels:
                output[l] = s[l]
                l += 1
            elif s[r].lower() not in vowels:
                output[r] = s[r]
                r -= 1
            else:
                output[r] = s[l]
                output[l] = s[r]
                l += 1
                r -= 1

        return "".join(output)